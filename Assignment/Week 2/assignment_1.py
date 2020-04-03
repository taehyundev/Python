import turtle

# 과제 2.2

birthDay = int(input("정수="))
birthDay_n1 =  birthDay // 1000
birthDay_n2 = (birthDay - (birthDay_n1 * 1000)) // 100 
birthDay_n3 = (birthDay - ((birthDay_n1 * 1000) + (birthDay_n2 * 100))) // 10
birthDay_n4 = birthDay % 10

print(birthDay_n1 + birthDay_n2 + birthDay_n3 +birthDay_n4)

# 공통 과제

#n에 입력
n = int(input("radius 값을 입력해주세요 : "))
t = turtle.Pen()
t.left(90)
t.forward(n/2)
# 반만큼 이동한후
t.circle(n/2)
# 지름이 n인 원을 그린다.
t.forward(n/2)
# 사각형 한변을 마저 채우고 진행
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
