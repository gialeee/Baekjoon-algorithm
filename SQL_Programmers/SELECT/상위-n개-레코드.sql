-- https://school.programmers.co.kr/learn/courses/30/lessons/59405
SELECT AI.NAME
FROM ANIMAL_INS AI
WHERE AI.DATETIME = (SELECT MIN(A.DATETIME)
                        FROM ANIMAL_INS A)
