# Write your MySQL query statement below
select b.employee_id, b.name, 
    count(a.reports_to) as reports_count, 
    round(avg(a.age)) as average_age
from Employees as b
join Employees as a
on b.employee_id = a.reports_to
group by b.employee_id,b.name
order by b.employee_id