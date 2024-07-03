import random

def rock_sissors_paper():
    rsp = ['가위', '바위', '보']
    computer = random.choice(rsp)
    win = 0
    drow = 0
    lose = 0

    while True:
        user = input('가위, 바위, 보 중에 하나를 선택하세요.:') # 여기에 가위, 바위, 보 중 한가지 입력.
        if user not in rsp:
            print('유효한 입력이 아닙니다.') # 가위, 바위, 보 범위 외 입력을 했을경우 오류메세지 출력.
            continue

        if (computer == rsp[1] and user == rsp[0]) or (computer == rsp[0] and user == rsp[2]) or (computer == rsp[2] and user == rsp[1]):
            print(f'컴퓨터는 {computer}를 냈다.')
            print('패배하였습니다.')
            lose += 1

        elif computer == user:
            print(f'컴퓨터는 {computer}를 냈다.')
            print('무승부 입니다.')
            drow += 1

        else:
            print(f'컴퓨터는 {computer}를 냈다.')
            print('당신이 이겼습니다!')
            win += 1

            try_again = input('다시 시작 하시겠습니까?(y / n): ') # 여기에 오류있음.
            if try_again == 'y':
                continue
            elif try_again == 'n':
                print('게임을 종료합니다.')
                print(f'승 : {win}, 무 : {drow} 패 : {lose}')
                break
            else:
                print('y와 n중에 입력하시오.')


rock_sissors_paper()