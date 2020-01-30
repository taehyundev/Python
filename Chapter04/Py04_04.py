a = [1,10,5,7,6]
a.reverse()
print(a)

#리스트를 뒤집어 준다. desc정렬이 아님

a = [1,10,5,7,6]
a.sort()
print(a)
#오름차순

a = [1,10,5,7,6]
a.sort(reverse=True)
print(a)
#내림차순 sort를 reverse해주는 것임

x = [1,11,2,3]
y = sorted(x)
print(y)
# 순서대로 정렬된 리스트를 반환 반환시켜줄때는 sorted

x = [1,11,2,3]
y = reversed(x)
print(y)
# 뒤집은  리스트를 반환 반환시켜줄때는 sorted
