# Write your MySQL query statement below
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
grp AS (
    SELECT *,
           id - rn AS group_id
    FROM cte
)

SELECT
    id,
    visit_date,
    people
FROM grp
WHERE group_id IN (
    SELECT group_id
    FROM grp
    GROUP BY group_id
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;