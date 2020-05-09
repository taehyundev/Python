from functools import reduce
#lamda 인자 : 표현식
def hap (x,y):
    return x+ y

print(hap(10,20))


## 위 함수를 람다를 사용해서 표현
print((lambda x,y: x + y)(10,20))

# 이 람다에서 반환되는 값들을 리스트화한다.
map(lambda x: x ** 2, range(5)) 

print(list(map(lambda x:x ** 2, range(5))))

# 반환값의 총합
print(reduce(lambda x,y: x + y, [0,1,2,3]))

print(reduce(lambda x,y: y + x, 'abcde'))

print(list(filter(lambda x: x -1 , [1,2,3,4])))
