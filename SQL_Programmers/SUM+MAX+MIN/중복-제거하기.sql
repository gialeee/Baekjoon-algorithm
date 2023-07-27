-- https://school.programmers.co.kr/learn/courses/30/lessons/59408
SELECT COUNT(DISTINCT AI.NAME) count
FROM ANIMAL_INS AI
WHERE AI.NAME IS NOT NULL
