s = ','.join(['가나','다라','마바'])
print(s)
#출력 : 가나,다라,마바
s = ' '.join(['가나','다라','마바'])
print(s)
#출력 : 가나 다라 마바

# '문자'.join을 할 시에 join안에 들어가는 문자열 리스트 요소들 사이에
# join앞에 설정한 문자가 들어가게 된다.

s = '가나,다라,마바'.split(',')
print(s)
# split같은 경우에는 split('문자')에 해당하는 문자를 기준으로 문자열이
# 리스트 형태로 분리되어 나누어진다.

departure, zz, arrival = "Seattle-Seoul".partition('-')
print(zz)
# partition같은 경우는 partition('문자') 의 문자를 기준으로 분배가 된다.
# 분배가 되면 Seattle , - , Seoul 이렇게 3개로 분해되서
# 선언한 변수의 순서에 맞게 departure = Seattle, zz = -, arrival = Seoul
# 각각 변수를 출력하면 위와 같이 나오는 것을 볼 수가 있다.


s = "Name: {0}, Age: {1}".format("강태현", 20)
print(s)

s = "Name: {name}, Age: {age}".format(name="강태현", age=20)
print(s)

area = (100, 200)
s = "x : {x[0]}, y : {x[1]}".format(x = area)
print(s)

# 여기서 여러 괄호들이 나오는데
# []리스트 정의 index, ()튜플 정의(추후 설명), {}집합(추후 설명)
# 순서에 맞게 포맷되고 또한 튜플의 정보 또한 순서에 맞게
# 포맷이 되는 것을 볼 수 있다.
