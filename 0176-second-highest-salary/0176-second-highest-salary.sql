# Write your MySQL query statement below
select ifnull(
    (select distinct salary 
    from Employee
    Order by salary DESC limit 1,1), null)as SecondHighestSalary