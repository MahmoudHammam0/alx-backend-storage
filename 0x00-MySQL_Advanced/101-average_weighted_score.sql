-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    JOIN (
        SELECT users.id, SUM(cor.score * proj.weight) / SUM(proj.weight) AS avg_weight
        FROM users
        JOIN corrections AS cor ON users.id = cor.user_id
        JOIN projects AS proj ON cor.project_id = proj.id
        GROUP BY users.id
    ) AS user_avg_weight ON users.id = user_avg_weight.id
    SET users.average_score = user_avg_weight.avg_weight;
END //

DELIMITER ;
