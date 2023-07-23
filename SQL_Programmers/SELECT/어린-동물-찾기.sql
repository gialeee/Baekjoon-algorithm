-- https://school.programmers.co.kr/learn/courses/30/lessons/59037
SELECT AI.ANIMAL_ID,
        AI.NAME
FROM ANIMAL_INS AI
WHERE 1=1
    AND AI.INTAKE_CONDITION <> 'Aged'
ORDER BY AI.ANIMAL_ID
