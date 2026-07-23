# Write your MySQL query statement below
select Distinct d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
Right JOIN Department d
On e.departmentId = d.id
JOIN (
    SELECT
        departmentId,
        MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) m
    ON e.departmentId = m.departmentId
   AND e.salary = m.max_salary;