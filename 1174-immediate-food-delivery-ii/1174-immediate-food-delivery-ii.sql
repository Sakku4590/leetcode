# Write your MySQL query statement below
select ROUND(
    100 * sum(
        case when d.order_date = d.customer_pref_delivery_date then 1
        else 0
        end
    )/count(*)
,2) as immediate_percentage
from Delivery as d
join(
    select customer_id, min(order_date) as first_order_date
    from Delivery
    group by customer_id
) f
where d.customer_id = f.customer_id
and d.order_date = f.first_order_date