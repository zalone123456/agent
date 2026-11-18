use learning_db;
SELECT* FROM topic_info;
SELECT* FROM study_records;
SELECT topic_info.topic,category,study_minutes
FROM topic_info LEFT JOIN study_records
on topic_info.topic=study_records.topic
WHERE study_records.id is NULL;

SELECT topic_info.topic,category,COUNT(study_records.id)
FROM topic_info LEFT JOIN study_records
on topic_info.topic=study_records.topic
GROUP BY topic_info.topic;


use learning_db;
SELECT * FROM study_records WHERE study_minutes>(SELECT AVG(study_minutes) FROM study_records);
SELECT * FROM study_records WHERE study_minutes=(SELECT MAX(study_minutes)FROM study_records);

SELECT * FROM study_records WHERE id=1;
START TRANSACTION;
UPDATE study_records SET study_minutes=study_minutes + 10 WHERE id=1;
SELECT * FROM study_records WHERE id=1;
COMMIT;
SELECT * FROM study_records WHERE id=1;