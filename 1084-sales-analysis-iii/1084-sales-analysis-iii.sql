# Write your MySQL query statement below
select p.product_id, p.product_name
from Product as p
WHERE p.product_id IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
)
AND p.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
);