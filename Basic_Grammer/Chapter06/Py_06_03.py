a = {'name': 'taehyundev', 'age':20, 'birth':1107}

print(a['name'], a['age'], a['birth'])

print(list(a.keys()))

#위의 함수를 통해서 key값을 볼 수 있다.

#리스트형식으로 반환을 원하면 위와 같이 list()에 넣으면 된다.

for k in a.keys():
    print(k)

# 위와같은 형태로 하나씩 key값을 뽑을 수 있다.

print(a.values())

#위의 함수를 통해서 value값을 볼 수 있다.
#위의 형태도 list()를 통해서 list형태로 반환할 수 있다.

print(a.items())

#위의 형태는 쌍을 튜플로 묶은 리스트 형태가 나온다.

a.clear()
print(a)
#clear를 사용하면 key value를 모두 지운다.

a = {'name': 'taehyundev', 'age':20, 'birth':1107}
print(a.get('name'))

#get()함수를 사용하면 key값을이용해서 value를 부를 수 있다.

print(a.get('aa'))
#없는걸 넣었을 때는 none을 반환한다.


print(a.get('aa','hey!'))
#aa가 없을 때 hey!가 출력되게 한다.
#a.get(x, '디폴트 값')


