num = int(input("정수 입력: "))
result = ""
for i in range(1, num+1):
    if i == 1 :
        result = str(num) + " 의 약수 : "
    if num % i == 0:
        result = result +" " + str(i)

print(result)

