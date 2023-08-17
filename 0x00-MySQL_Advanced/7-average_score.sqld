-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    
    -- Calculate total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;
    
    -- Calculate total number of projects for the user
    SELECT COUNT(*) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;
    
    -- Update average score for the user
    UPDATE users
    SET average_score = IF(total_projects > 0, total_score / total_projects, 0)
    WHERE id = user_id;
END;
//

DELIMITER ;

