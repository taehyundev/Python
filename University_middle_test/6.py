'''
number = 235
s =0 

while number > 1:
    d = number % 10
    s = s+ d
    number = number //d

print(s)
'''
# 실행 결과 18

'''
word = 'beautiful'
print(word[2:5] + 'umn', 4+5)
'''
# 실행 결과 autumn 9

'''
def ft(n):
    if n % 2 == 0:
        for k in range(1,n):
            if k % 5 == 0:
                print(k, end = ' ')
    else:
        for k in range(1,n):
            if k % 3 == 0:
                print(k, end = ' ')

ft(15)
'''
# 실행 결과 3 6 9 12
'''
i = 2
j = 1
k = 3

if i > j:
    if i > k :
        print('A')
else:
    print('B')
print('C')
'''
# 실행 결과 C

def ft(m):
    m = [1,2,3]
    return
m = [10,20,30]
ft(m)
print(m)

# 실행결과 [10, 20, 30]