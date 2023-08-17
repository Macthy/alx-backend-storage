#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    print("Methods:")
    for method in methods:
        count_method = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count_method}")

    # Count status check with method=GET and path=/status
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status_check_count} status check")
