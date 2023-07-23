-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
SELECT COUNT(*) USERS
FROM USER_INFO UI
WHERE UI.AGE BETWEEN 19 AND 29
    AND DATE_FORMAT(UI.JOINED, '%Y') = 2021
