# Write your MySQL query statement below
-- select c.name as Customers
-- from Customers c
-- left join Orders o
-- on c.id = o.customerID
-- where o.customerID is null

select name as Customers
from Customers
where id not in(
    select customerID
    from Orders
)