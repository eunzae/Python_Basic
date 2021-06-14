# Section04-2
# 문자열, 문자열 연산, 슬라이싱


# 문자열 생성
str1 = "I am a Boy."
str2 = 'Niceman'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))


escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \t Tab"
print(escape_str2)

# Raw String: r 뒤에 오는 문자는 escape 문자로 인식하지 않음
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)


# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# 참고: https://www.w3schools.com/python/python_ref_string.asp

a = 'Niceman'
b = 'oranges'
print(a.islower()) # 대문자 포함하면 false 반환
print(b.endswith('s')) # 끝 글자가 해당 글자로 끝나는지 확인
print(b.capitalize()) # 문자열의 첫 글자 대문자로 변환
print(a.replace('Nice','Good'))
print(list(reversed(b)))


# 슬라이싱
print(a[0:3])
print(a[0:4])
print(a[0:len(a)-1])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])
