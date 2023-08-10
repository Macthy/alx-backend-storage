-- Create the ComputeAverageWeightedScoreForUsers stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_users INT;
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE user_weighted_score FLOAT;

    -- Get the total number of users
    SELECT COUNT(*) INTO total_users FROM users;

    -- Loop through each user
    SET user_id = 1;
    WHILE user_id <= total_users DO
        -- Calculate the weighted average score for the user
        SET total_weighted_score = 0;
        SELECT SUM(score * weight) INTO total_weighted_score
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        SET user_weighted_score = total_weighted_score / (SELECT SUM(weight) FROM projects);

        -- Update the user's average_score
        UPDATE users
        SET average_score = user_weighted_score
        WHERE id = user_id;

        -- Move to the next user
        SET user_id = user_id + 1;
    END WHILE;
END;
//

DELIMITER ;

