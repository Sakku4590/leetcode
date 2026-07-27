# Write your MySQL query statement below
select t.request_at as 'Day',
Round(sum(
    case when t.status != 'completed' then 1
    else 0
    END)/count(*),
    2
) as 'Cancellation Rate'
From Trips as t
Join Users as c
On t.client_id = c.users_id
join Users as d
on t.driver_id = d.users_id
where c.banned = 'No'
and d.banned = 'No'
and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at
