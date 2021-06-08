# Section02
# 파이썬 소개 및 작업 환경 설정


# 기본 출력
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

# separator 옵션 사용
print('T','E','S','T')
print('T','E','S','T', sep='')
print('2019','02','19',sep='-') # 공백에 작은따옴표 안 문제 입력
print('niceman','google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')

# format 사용 [] . {} , ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print('{a} and {b}'.format(a='You', b='Me'))

# % 사용
# 데이터 형태까지 지정 가능하므로 코딩 면에서 가장 정확함
# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Eunjae', 4))

# 실습
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))


# Escape 코드
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""
# 'You'를 출력하고 싶을 때
# print(''You'') # ERROR
print("'You'") #'You'
print('\'You\'') #'You'
print("""'You'""")
print('"You"')
print('\\You\\')
print('You\n')
print('\t\t\tYou')