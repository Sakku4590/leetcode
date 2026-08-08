# Write your MySQL query statement below
select 
    l.book_id, 
    l.title, 
    l.author, 
    l.genre, 
    l.publication_year, 
    COUNT(*) AS current_borrowers
from library_books as l
join borrowing_records as b
    on l.book_id = b.book_id
where b.return_date is NULL
group by l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    l.total_copies
having count(*) = l.total_copies
order by current_borrowers DESC,
    l.title ASC

