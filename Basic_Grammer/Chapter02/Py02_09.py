n = int(input("구구단 : "))
for i in range(1, n+1):
    print("<",i,"단>")
    for j in range(1,10):
        print(i ," * ", j ," = ", (i*j))
    print()