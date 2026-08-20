# Write your MySQL query statement below
WITH FirstPositive AS (
    -- Find the earliest positive test date for each patient
    SELECT patient_id, MIN(test_date) AS first_pos_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
FirstNegativeAfterPositive AS (
    -- Find the earliest negative test date that occurs AFTER the first positive test
    SELECT fp.patient_id, fp.first_pos_date, MIN(ct.test_date) AS first_neg_date
    FROM FirstPositive fp
    INNER JOIN covid_tests ct 
        ON fp.patient_id = ct.patient_id 
        AND ct.result = 'Negative' 
        AND ct.test_date > fp.first_pos_date
    GROUP BY fp.patient_id, fp.first_pos_date
)
-- Join with the patients table to pull names and age, and calculate the difference
SELECT 
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(fn.first_neg_date, fn.first_pos_date) AS recovery_time
FROM patients p
INNER JOIN FirstNegativeAfterPositive fn 
    ON p.patient_id = fn.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;