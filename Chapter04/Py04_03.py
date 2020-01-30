#list 원소의 추가 및 삭제

#list 원소 추가
a = [1,2,3,4,5]
a.append(7.5)
print(a)

#append는 list의 원소 뒷쪽에 추가 시켜준다.

a = [1,2,3]
a.insert(1,5)
print(a)

#insert(index위치, 값) index위치에 값을 추가시켜준다.


a = [1,2,3]
a.extend([4,5,6])
print(a)

#extend를 이용해서 리스트를 추가할 수 있다.


#list 원소 삭제
a= [1,2,3,4,5,6,7]
del a[1]
print(a)

#a[i] a의 i번째 인덱스를 del를 통해서 삭제한다.

a= [1,2,3,4,5,6,7]
a.remove(3)
print(a)

#del과는 달리 index가 아니라 그 값 자체를 찾아서 지워준다.
#찾을 아이템이 없으면 오류가 발생함



###del과 index 메소드를 혼합해서 remove 효과내기
a = [1,2,3,4,5,6,7]
del a[a.index(7)]
print(a)
