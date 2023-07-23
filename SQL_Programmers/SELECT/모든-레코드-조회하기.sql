-- https://school.programmers.co.kr/learn/courses/30/lessons/59034
SELECT AI.ANIMAL_ID,
        AI.ANIMAL_TYPE,
        AI.DATETIME,
        AI.INTAKE_CONDITION,
        AI.NAME,
        AI.SEX_UPON_INTAKE
FROM ANIMAL_INS AI
ORDER BY ANIMAL_ID
