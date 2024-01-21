# 문자열 str
# 문자열 자료형. 기본적으로 따옴표로 묶어서 데이터를 ㅍ표현
# 문자열을 한 글자이거나 여러 글자여도 작은 따옴표(')와 큰 따옴표(")를 모두 사용할 수 있다.
# 각 따옴표를 3개씩 사용하는 삼둥 따옴표(''' ''', """ """)
# snigle line : 한 줄의 문자열 : 작은 따옴표(')와 큰 따옴표(")
# multiple Line : 여러줄의 문자열 : 삼중 따옴표(''' '''.""" """)

# 문자열 벼노한
# str() 함수를 사용하면 다른 자료형의 값을 문자열 데이터로 변환 할 수있다.
print(str(100)) # '100' / 정수 100을 문자열 '100'으로 변환
print(str(True)) # 'True' / 논리형 True를 문자열 'True)로 변환
print(str(False)) # 'False' / 논리형 Flase 문자열 'Flase)로 변환
print(type(str(3.14))) # <class 'str'> / 타입을 받았기 떄문에 string이 찍힌다.

# 문자열 인덱싱 indexing
# 0번부터 시작
print()
s = 'hello'
print(s[1]) # e
# 마이너스(-) 인덱스는 문자열 뒤에서 부터 부여, 마지막 인덱스는 -1이 된다.
print(s[1] == s[-4]) # True
print(s[-5])
print(s[0])
print(s[-5] == s[0]) # True

# 문자열 슬라이싱 slicing
# 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용
# s[star:stop:step]
# stop :  종료 인덱스를 지정, 생락하면 끝까지 추출
# step : 인덱스의 증감값, 생략하면 1씩 변화
print()
s = ('banana')
print(s[0:3]) # ban / 종료 인덱스는 포함 X
print(s[0:6:2]) # bnn
print(s[0:5:3]) # ba
print(type(s)) # <class 'str'>

print(s[-1:]) # [-1:] : 끝까지 출력해라