-- https://school.programmers.co.kr/learn/courses/30/lessons/59036
SELECT AI.ANIMAL_ID,
        AI.NAME
FROM ANIMAL_INS AI
WHERE 1=1
    AND AI.INTAKE_CONDITION = 'Sick'
ORDER BY AI.ANIMAL_ID
