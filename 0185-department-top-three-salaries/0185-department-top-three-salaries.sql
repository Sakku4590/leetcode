# Write your MySQL query statement below
select Dep.name as Department, Emp.name as Employee, Emp.salary as Salary
from Employee as Emp
join Department as Dep
on Emp.departmentId = Dep.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = Emp.departmentId
      AND e2.salary > Emp.salary
) < 3; 