-- This file calculates average score for a student
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser (
    IN user_id INT
)

BEGIN
    DECLARE total_score FLOAT;
    DECLARE no_of_projects INT;
    DECLARE _average FLOAT;
    SELECT SUM(score) INTO total_score FROM corrections
    WHERE corrections.user_id = user_id;
    -- Computing the average score...
    SELECT COUNT(project_id) INTO no_of_projects
    FROM corrections
    WHERE corrections.user_id = user_id;
    -- Updating table with new data...
    SET _average = total_score / no_of_projects;
    UPDATE users SET average_score = _average
    WHERE id = user_id;
END$$
DELIMITER ;
