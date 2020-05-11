def ft(c):
    s = 'Beautiful Sunday'
    cnt =0
    for i in range(0, len(s)):
        if s[i] == c:
            print(str(i+1)+" 번째 "+c+" 발견")
            cnt = cnt +1
    return cnt


ch = input('찾는 문자: ')
total = ft(ch)
print("총 문자 수: "+ str(total))

