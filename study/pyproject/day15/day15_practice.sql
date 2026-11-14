USE learning_db;


-- 查看全部学习记录
SELECT * FROM study_records;

-- 将 id 为 2 的记录改为 90 分钟
-- 注意：你目前已经删除 id=2，练习时先确认要修改的 id
UPDATE study_records
SET study_minutes = 90
WHERE id = 2;

-- 删除 id 为 2 的记录
-- 注意：删除前先用 SELECT 确认目标记录
DELETE FROM study_records
WHERE id = 2;

-- 只查看学习主题和分钟数
SELECT topic, study_minutes
FROM study_records;

-- 查询主题为 Python 的记录
SELECT * FROM study_records
WHERE topic = 'Python';

-- 查询学习时间不少于 45 分钟的记录
SELECT * FROM study_records
WHERE study_minutes >= 45;

-- 查询主题为 Python，并且学习时间不少于 45 分钟的记录
SELECT * FROM study_records
WHERE topic = 'Python' AND study_minutes >= 45;

-- 查询主题为 Python 或 Git 的记录
SELECT * FROM study_records
WHERE topic IN ('Python', 'Git');

-- 查询备注中包含“复习”的记录
SELECT * FROM study_records
WHERE notes LIKE '%复习%';

-- 查询没有填写备注的记录
SELECT * FROM study_records
WHERE notes IS NULL;

-- 按学习分钟数从高到低排序
SELECT * FROM study_records
ORDER BY study_minutes DESC;

-- 第一页：按 id 排序，跳过 0 条，最多取 3 条
SELECT * FROM study_records
ORDER BY id ASC
LIMIT 3 OFFSET 0;

-- 第二页：按 id 排序，跳过前 3 条，最多取 3 条
SELECT * FROM study_records
ORDER BY id ASC
LIMIT 3 OFFSET 3;