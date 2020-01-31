# 교집합 합집합 차집합 구하기

s1 = set([4,1,2,3,14,2,1])
s2 = set([1,4,5,3,6,9,32])

# 교집합
print(s1& s2)

print(s1.intersection(s2))
## 둘다 같은 결과


# 합집합
print(s1|s2)


print(s1.union(s2))
## 둘 다 같은 결과


# 차집합(2가지 경우)
print(s1-s2) #s1 기준
print(s2-s1) #s2 기준

print(s1.difference(s2))
print(s2.difference(s1))
## 둘다 같은 기능

