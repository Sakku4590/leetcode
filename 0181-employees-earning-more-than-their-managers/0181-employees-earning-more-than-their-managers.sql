# Write your MySQL query statement below

SELECT A.name AS Employee
FROM Employee A
JOIN Employee B
on A.managerID = B.id
WHERE A.salary > B.salary

