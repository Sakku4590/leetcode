# Write your MySQL query statement below
select Emp.name, B.bonus 
from employee Emp
left join Bonus B
ON Emp.empId = B.empId
where B.bonus < 1000 or B.bonus Is null
    
