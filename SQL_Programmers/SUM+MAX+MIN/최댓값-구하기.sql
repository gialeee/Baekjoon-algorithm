-- https://school.programmers.co.kr/learn/courses/30/lessons/59415
SELECT AI.DATETIME '시간'
FROM ANIMAL_INS AI
WHERE AI.DATETIME = (SELECT MAX(DATETIME)
                        FROM ANIMAL_INS)
