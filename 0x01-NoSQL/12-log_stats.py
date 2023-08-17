#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

def print_stats():
    client = MongoClient('mongodb://localhost:27017/')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    # Count total number of logs
    total_logs = nginx_collection.count_documents({})

    print(f"{total_logs} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count status check with method=GET and path=/status
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    print_stats()
