# Write your MySQL query statement below
select s.user_id,
    ROUND(
        IFNULL(
            SUM(CASE WHEN c.action = 'timeout' THEN 0 ELSE 1 END) / COUNT(c.action),
            0
        ),
        2
    ) AS confirmation_rate
from Signups as s
left join Confirmations as c
on s.user_id = c.user_id
group by s.user_id
