# Write your MySQL query statement below
select ROUND(
    count(a.player_id)/
    (select count(distinct player_id) from Activity),
    2
)as fraction
from Activity a
join(
    select player_id, min(event_date) as first_login
    from Activity
    group by player_id
)first_day
on a.player_id = first_day.player_id
AND a.event_date = DATE_ADD(first_day.first_login, interval 1 day)