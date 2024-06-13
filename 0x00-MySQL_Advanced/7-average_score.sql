-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
        IN user_id INT
)

BEGIN
        DECLARE projects_num INT;
        DECLARE score_sum INT;

        SELECT COUNT(project_id) 
		INTO projects_num 
		FROM corrections 
		WHERE corrections.user_id = user_id;
        SELECT SUM(score) 
		INTO score_sum
		FROM corrections
		WHERE corrections.user_id = user_id;

	UPDATE users
		SET users.average_score = IF(projects_num = 0, 0, score_sum / projects_num)
		WHERE users.id = user_id;
END;

//

DELIMITER ;
