-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_weighted_score FLOAT;

    SELECT AVG(score * weight) INTO avg_weighted_score
    FROM scores
    WHERE user_id = user_id;

    INSERT INTO average_scores (user_id, average_weighted_score, calculated_at)
    VALUES (user_id, avg_weighted_score, NOW());
END //

DELIMITER ;
