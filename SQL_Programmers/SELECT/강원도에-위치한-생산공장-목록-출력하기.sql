-- https://school.programmers.co.kr/learn/courses/30/lessons/59034
SELECT FF.FACTORY_ID,
        FF.FACTORY_NAME,
        FF.ADDRESS
FROM FOOD_FACTORY FF
WHERE FF.ADDRESS LIKE "강원도%"
ORDER BY FF.FACTORY_ID