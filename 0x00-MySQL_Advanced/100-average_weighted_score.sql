-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_scores FLOAT;

    SELECT SUM(C.score * P.weight) / SUM(P.weight)
    INTO weighted_scores
    FROM corrections AS correct
    JOIN projects AS proj ON correct.project_id = proj.id
    WHERE correct.user_id = user_id;

    UPDATE users
    SET average_score = weighted_scores
    WHERE id = user_id;

END //

DELIMITER ;
