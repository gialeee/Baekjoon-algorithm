'''
Programmers SQL 코딩테스트 문제 풀이 내용 .sql 파일로 변환
'''

# 문제 관련 정보
path = "./SELECT/"
title = "3월에 태어난 여성 회원 목록 출력하기"
url = "https://school.programmers.co.kr/learn/courses/30/lessons/131120"
query = """
SELECT MP.MEMBER_ID,
        MP.MEMBER_NAME,
        MP.GENDER,
        DATE_FORMAT(MP.DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE MP
WHERE MP.GENDER = 'W'
    AND MONTH(MP.DATE_OF_BIRTH) = 3
    AND MP.TLNO IS NOT NULL
ORDER BY MP.MEMBER_ID
"""

# sql 파일 생성
filepath = path + title.replace(" ", "-") + ".sql"
content = "-- " + url + query

try:
    with open(filepath, 'w') as f:
        f.write(content)
        print(filepath, "에 파일이 생성되었습니다.")
except FileNotFoundError:
    print("해당 경로를 찾을 수 없습니다.")