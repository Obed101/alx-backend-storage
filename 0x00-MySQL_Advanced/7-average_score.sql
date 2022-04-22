-- This file calculates average score for a student
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser (
    IN user_id INT
)

BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (
        SELECT AVG(score) FROM corrections
        WHERE id = user_id
    );
    UPDATE users SET average_score = avg_score
    WHERE id = user_id;
END$$
