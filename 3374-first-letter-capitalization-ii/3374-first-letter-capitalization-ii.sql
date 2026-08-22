WITH RECURSIVE cte AS (
    SELECT 
        content_id,
        content_text,
        1 AS pos,
        CAST('' AS CHAR(2000)) AS converted
    FROM user_content

    UNION ALL

    SELECT
        c.content_id,
        c.content_text,
        c.pos + 1,
        CONCAT(
            c.converted,
            CASE
                WHEN SUBSTRING(c.content_text, c.pos, 1) REGEXP '[A-Za-z]' THEN
                    CASE
                        WHEN c.pos = t.tokenStart 
                            THEN UPPER(SUBSTRING(c.content_text, c.pos, 1))
                        WHEN c.pos > 1
                             AND SUBSTRING(c.content_text, c.pos-1, 1) = '-'
                             AND t.hyphenCount = 1
                             AND (c.pos-1) > t.tokenStart
                             AND SUBSTRING(c.content_text, c.pos-2, 1) REGEXP '[A-Za-z]'
                            THEN UPPER(SUBSTRING(c.content_text, c.pos, 1))
                        ELSE LOWER(SUBSTRING(c.content_text, c.pos, 1))
                    END
                ELSE SUBSTRING(c.content_text, c.pos, 1)
            END
        ) AS converted
    FROM cte c
    CROSS JOIN LATERAL (
        SELECT
            bounds.ts AS tokenStart,
            CHAR_LENGTH(SUBSTRING(c.content_text, bounds.ts, bounds.te - bounds.ts + 1))
              - CHAR_LENGTH(REPLACE(SUBSTRING(c.content_text, bounds.ts, bounds.te - bounds.ts + 1), '-', '')) AS hyphenCount
        FROM (
            SELECT
                (CASE WHEN LOCATE(' ', REVERSE(SUBSTRING(c.content_text,1,c.pos-1))) = 0 
                      THEN 1 
                      ELSE c.pos - LOCATE(' ', REVERSE(SUBSTRING(c.content_text,1,c.pos-1))) + 1 
                 END) AS ts,
                (CASE WHEN LOCATE(' ', SUBSTRING(c.content_text, c.pos)) = 0 
                      THEN CHAR_LENGTH(c.content_text) 
                      ELSE c.pos + LOCATE(' ', SUBSTRING(c.content_text, c.pos)) - 2 
                 END) AS te
        ) bounds
    ) t
    WHERE c.pos <= CHAR_LENGTH(c.content_text)
)
SELECT 
    content_id,
    content_text AS original_text,
    converted AS converted_text
FROM cte
WHERE pos = CHAR_LENGTH(content_text) + 1
ORDER BY content_id;