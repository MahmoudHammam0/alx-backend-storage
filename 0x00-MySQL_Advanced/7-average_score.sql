-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
        IN user_id INT
)

BEGIN
        DECLARE projects_num INT;
        DECLARE score_sum INT;
        DECLARE avgscore DECIMAL;

        SELECT COUNT(project_id) 
		INTO projects_num 
		FROM corrections 
		WHERE corrections.user_id = user_id;
        SELECT SUM(score) 
		INTO score_sum
		FROM corrections
		WHERE corrections.user_id = user_id;

        IF projects_num > 0 THEN
                SET avgscore = score_sum / projects_num;
        ELSE
                SET avgscore = 0;
        END IF;

        UPDATE users SET average_score = avgscore WHERE id = user_id;
END;

//

DELIMITER ;
