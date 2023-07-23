-- https://school.programmers.co.kr/learn/courses/30/lessons/59404
SELECT AI.ANIMAL_ID,
        AI.NAME,
        AI.DATETIME
FROM ANIMAL_INS AI
ORDER BY AI.NAME, AI.DATETIME DESC
