n = int(input("별찍기 : "))
for i in range(1, n+1):
    print(" " * (n-i), "*" * (i))