exersize = dict()
while True:
    print("1. 운동 종류 시간 추가")
    print("2. 운동 종류 삭제")
    print("3. 운동 리스트")
    print("4. 종료")
    sw = int(input("메뉴를 입력하시오: "))
    if sw == 1:
        kind = input("운동 종류 입력: ")
        time = input("운동 시간 입력: ")
        exersize[kind] = time
        print(exersize)
    elif sw == 2:
        kind = input("운동 종류 입력: ")
        del exersize[kind]
    elif sw == 3:
        print(exersize)
    elif sw == 4:
        break