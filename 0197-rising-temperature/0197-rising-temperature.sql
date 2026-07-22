# Write your MySQL query statement below
select t.id as id
from Weather t
JOIN Weather y
on DATEDIFF(t.recordDate, y.recordDate) = 1
where t.temperature > y.temperature