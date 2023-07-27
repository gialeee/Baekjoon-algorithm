-- https://school.programmers.co.kr/learn/courses/30/lessons/131115
SELECT FP.PRODUCT_ID,
    FP.PRODUCT_NAME,
    FP.PRODUCT_CD,
    FP.CATEGORY,
    FP.PRICE
FROM FOOD_PRODUCT FP
WHERE FP.PRICE = (SELECT MAX(F.PRICE)
                    FROM FOOD_PRODUCT F)
