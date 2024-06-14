-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weight FLOAT;

    SELECT SUM(C.score * P.weight) / SUM(P.weight)
    INTO avg_weight
    FROM corrections AS C
    JOIN projects AS P ON C.project_id = P.id
    WHERE C.user_id = user_id;

    UPDATE users
    SET average_score = avg_weight
    WHERE id = user_id;
END //

DELIMITER ;
