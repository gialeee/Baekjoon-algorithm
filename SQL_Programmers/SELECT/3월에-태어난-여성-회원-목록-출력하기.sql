-- https://school.programmers.co.kr/learn/courses/30/lessons/131120
SELECT MP.MEMBER_ID,
        MP.MEMBER_NAME,
        MP.GENDER,
        DATE_FORMAT(MP.DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE MP
WHERE MP.GENDER = 'W'
    AND MONTH(MP.DATE_OF_BIRTH) = 3
    AND MP.TLNO IS NOT NULL
ORDER BY MP.MEMBER_ID
