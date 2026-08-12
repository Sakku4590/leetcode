# Write your MySQL query statement below
select p.product_id, COALESCE(pr.new_price,10) as price
from (SELECT DISTINCT product_id FROM Products) p
left join Products as pr
on p.product_id = pr.product_id
    and pr.change_date = (
        select max(change_date)
        from Products
        WHERE product_id = p.product_id
        AND change_date <= '2019-08-16'
    )
