-- https://school.programmers.co.kr/learn/courses/30/lessons/151136
SELECT ROUND(AVG(DAILY_FEE)) 'AVERAGE_FEE'
FROM CAR_RENTAL_COMPANY_CAR C
WHERE C.CAR_TYPE = 'SUV'
