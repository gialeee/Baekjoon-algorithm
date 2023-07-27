-- https://school.programmers.co.kr/learn/courses/30/lessons/59038
SELECT AI.DATETIME '시간'
FROM ANIMAL_INS AI
WHERE AI.DATETIME = (SELECT MIN(DATETIME)
                        FROM ANIMAL_INS)
