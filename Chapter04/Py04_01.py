#list
#list는 순서가 있는 수정가능한 객체의 집합이다.
#수정 삭제 추가가 가능 , 일반 코딩 언어의 배열처럼 보면됨
# [] << 괄호를 사용

a = [3,15,12,4]
for i in range(0,4):
    print(a[i])

a = ['a', 3, True]
for i in range(0,3):
    print(a[i])

# 여러 타입을 섞어서 제작가능하다.

#추가
print()
print("추가")
a = []
print(a)
a.append(5)
a.append('a')
print(a)

# append로 추가가 가능하다.

a = [1,3,5]
b = [2,7]
c = a + b
print (c)

# + 연산자를 통해서 list를 합칠 수도 있다.
