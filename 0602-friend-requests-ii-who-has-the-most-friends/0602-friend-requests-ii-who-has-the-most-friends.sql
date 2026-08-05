# Write your MySQL query statement below
WITH AllFriends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)SELECT id, count(*) as num
FROM AllFriends
group by id
order by num desc
limit 1