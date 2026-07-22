# Write your MySQL query statement below
Select emp.name as Employee from Employee as emp Join employee as mgr 
on emp.managerId = mgr.id
where emp.salary > mgr.salary