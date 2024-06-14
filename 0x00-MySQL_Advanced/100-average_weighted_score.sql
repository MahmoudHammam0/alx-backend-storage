-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weight FLOAT;

    SELECT SUM(cor.score * proj.weight) / SUM(proj.weight)
    INTO avg_weight
    FROM corrections AS cor
    JOIN projects AS proj ON cor.project_id = proj.id
    WHERE cor.user_id = user_id;

    UPDATE users
    SET average_score = avg_weight
    WHERE id = user_id;
END //

DELIMITER ;
