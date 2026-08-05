# Write your MySQL query statement below
select r.contest_id, 
    round(count(r.user_id) * 100/(select count(*) from Users),2) as percentage
from Register as r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC