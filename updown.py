import random

def up_down_game():
    computer = random.randint(1, 100)
    count = 0

    while True:
        try:
            user = int(input('1부터 100까지의 숫자를 입력하세요.: ')) # 여기에 숫자 입력
        except ValueError:
            print('숫자로 입력해 주세요.') # 에러메세지
            continue
        if user > 100 or user < 0:
            print('유효한 범위 내의 숫자를 입력하세요.')
            continue
        count += 1
        # print(f'{count}번 시도하였습니다.') # 시도 횟수를 보여줌

        if user > computer:
            print('UP. 수가 너무 큽니다.')

        elif user < computer:
            print('DOWN. 수가 너무 작습니다.')

        else:
            print('정답입니다!')
            print(f'{count}번 만에 맞추셨습니다!')
            try_again = input('다시 하시겠습니까?: ') # 여기에 y, n중 한가지 입력(글자)
            if try_again == 'y':
                print('게임을 다시 시작합니다.')
                continue
            elif try_again == 'n':
                print('게임을 종료합니다.')
                break # 반복문 종료
up_down_game()










