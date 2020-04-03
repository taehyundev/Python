#집합 자료형 관련 함수들

s1 = set([1,2,3])
s1.add(4)
print(s1)
#add를 통해서 집합의 원소를 추가 시킬 수 있다.
#한개의 값만 추가할 때는 add를 사용

s1.update([5,6,7])
print(s1)
#update를 통해서 여러개를 추가

s1.remove(7)
print(s1)
#7이라는 값을 없애준다.
#하나만 가능