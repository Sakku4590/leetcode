# Write your MySQL query statement below
select ifnull(
    (select num
    from MyNumbers
    group by num 
    having count(num) < 2
    order by num Desc limit 0,1
    ),null
)as num