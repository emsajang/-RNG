# 라이브러리
import random
import time
import os

# 변수
loanLimit = 100000
money = 5000
speed = 0.05
totLoan = 0
count = 0
usercoin = 0
n1 = 0
n2 = 0
n3 = 0

# 리스트
slot = []
math = []
nomoney = ['돈이 없음 썩 꺼지거라.','분명 말했다. 돈 없음 가라.','마지막 경고다. 돈이 없더냐? 그럼 나가라.','...']
slotIcon = ['🍋','🍒','🍓','🍇','⭐️','💎','🍀','💰']
앞뒤 = ['앞', '뒷']
앞뒤1 = ['앞', '뒤']

# typrint
def typrint(text, sleep=float(0.25), delay = None, end = None):
    if delay is None:
        delay = float(speed)
    
    if end is None:
        end = '\n'

    for chat in text:
        print(chat, end='', flush=True)
        time.sleep(delay)
    print(end = end, flush=True)
    time.sleep(sleep)
# tyinput
def tyinput(prompt, delay = None):
    if delay is None:
        delay = float(speed)

    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()
# gameOver
def gameOver():
    typrint(f'최종 금액: {money}원',0.5)
    typrint('☠️ 게 임 오 버 ☠️',0.25,0.15)

# clear
def clear():
    os.system('cls')

# triDotText
def triDotText(text):
    typrint(f'{text}',end = '')
    typrint('...', delay = 0.75, end = '')


#---MainGame---#
clear()
time.sleep(0.5)
while True: # --시작화면--
    typrint('라이프슬롯v1.3에 오신 것을 환영합니다.\n')
    mainMenu = tyinput('------로비------\n1. 게임시작\n2. 설정\n3. 제작자\n4. 종료\n')
    if mainMenu in ['4', '종료']:
        clear()
        gameOver()
        break
    elif mainMenu in ['3', '제작자']:
        clear()
        typrint('Made by Ang임사장')
        clear()
        continue
    elif mainMenu in ['2', '설정']:
        clear()
        while True:
            settings = tyinput('------설정------\n1. 대사 속도\n2. 대출 한도\n3. 돌아가기\n')
            if settings in ['3', '돌아가기']:
                clear()
                break
            if settings in ['2', '대출 한도']:
                while True:
                    clear()
                    setLoanLimit = int(tyinput(f'기존 대출 한도: {loanLimit}원\n새로운 대출 한도를 입력하세요: '))
                    if setLoanLimit < 0:
                        clear()
                        typrint('올바른 금액을 입력하세요.',sleep = 1)
                        clear()
                        continue
                    else:
                        loanLimit = setLoanLimit
                        clear()
                        triDotText(f'대출 한도가 {loanLimit}원으로 설정되었습니다')
                        clear()
                        break
            if settings in ['1', '대사 속도']:
                clear()
                while True:
                    settingSpeed = tyinput('------대사 속도 설정------\n1. 빠르게\n2. 보통\n3. 느리게\n4. 사용자 지정\n5. 돌아가기\n')
                    if settingSpeed in ['5', '돌아가기']:
                        clear()
                        break
                    elif settingSpeed in ['4', '사용자 지정']:
                        clear()
                        speed = float(tyinput('사용자 지정 속도를 입력하세요 (default: 0.05): '))
                        triDotText(f'대사 속도가 {speed}으로 설정되었습니다')
                        clear()
                        continue
                    elif settingSpeed in ['3', '느리게']:
                        clear()
                        speed = 0.1
                        triDotText(f'대사 속도가 {'느리게'}로 설정되었습니다')
                        clear()
                        continue
                    elif settingSpeed in ['2', '보통']:
                        clear()
                        speed = 0.05
                        triDotText(f'대사 속도가 {'보통'}으로 설정되었습니다')
                        clear()
                        continue
                    elif settingSpeed in ['1', '빠르게']:
                        clear()
                        speed = 0.0075
                        triDotText(f'대사 속도가 {'빠르게'}로 설정되었습니다')
                        clear()
                        continue
                if settings not in ['1', '2', '3', '대사 속도', '대출 한도', '돌아가기']:
                    clear()
                    typrint('잘못된 선택입니다.',sleep = 1)
                    clear()
                    continue
    elif mainMenu in ['1', '게임시작']:
        clear()
        triDotText(f'\n 고작 {money}원만 가진 채 길거리로 떠납니다')
        while True: # --메인메뉴--
            clear()
            inGame1 = tyinput('------길거리------\n1. 임사장 카지노\n2. 돈벌기\n3. 임금은행\n4. 통계\n5. 돌아가기\n')
            if inGame1 in ['5', '돌아가기']:
                while True:    
                    returntostart = tyinput('정말로 돌아가시겠습니까? (Y/N) : ')
                    if returntostart in ['Y', 'y']:
                        clear()
                        break
                    elif returntostart in ['N', 'n']:
                        clear()
                        break
                    elif returntostart not in ['Y', 'y', 'N', 'n']:
                        clear()
                        typrint('Y or N 을(를) 입력하세요.',sleep = 1)
                        continue
                if returntostart in ['Y', 'y']:
                    break
                elif returntostart in ['N', 'n']:
                    continue
            elif inGame1 in ['4', '통계']:#추가예정
                clear()
                
                continue
            elif inGame1 in ['3', '임금은행']: #추가예정
                clear()
                triDotText('\n 임금은행으로 이동합니다')
                clear()
                while True:    
                    clear()
                    bankChoice = tyinput('------임금은행------\n1. 대출\n2. 환전\n3. 대출 정보\n4. 돌아가기\n')
                    if bankChoice in ['4', '돌아가기']:
                        clear()
                        triDotText('\n 길거리로 돌아갑니다')
                        clear()
                        break
                    elif bankChoice in ['3', '대출 정보']:
                        clear()
                        typrint(f'현재 대출 한도: {loanLimit}원\n총 대출 금액: {totLoan}원')
                    elif bankChoice in ['2', '환전']:
                        while True:
                            clear()
                            exchangeAmount = int(tyinput('환전할 금액을 입력하세요: '))
                            if exchangeAmount <= 0:
                                clear()
                                typrint('올바른 금액을 입력하세요.',sleep = 1)
                                clear()
                                continue
                            elif exchangeAmount > money:
                                clear()
                                typrint('환전 금액이 보유한 코인보다 많습니다.')
                                clear()
                                continue
                            else:
                                money -= exchangeAmount
                                typrint(f'{exchangeAmount}원 환전이 완료되었습니다. 현재 잔액: {money}원')
                    elif bankChoice in ['1', '대출']:
                        while True:
                            clear()
                            loanChoice = tyinput('1. 대출받기\n2. 상환하기\n3. 돌아가기\n')
                            if loanChoice in ['3', '돌아가기']:
                                clear()
                                break
                            if loanChoice in ['2', '상환하기']:
                                while True:
                                    clear()
                                    repayAmount = int(tyinput(f'현재 대출 금액: {totLoan}원\n상환 금액을 입력하세요: '))
                                    if repayAmount <= 0:
                                        typrint('\n올바른 금액을 입력하세요.',sleep = 1)
                                        clear()
                                        continue
                                    elif repayAmount > totLoan:
                                        typrint('\n상환 금액이 대출 금액보다 많습니다.',sleep = 1)
                                        clear()
                                        continue
                                    elif repayAmount > money:
                                        typrint('\n보유한 금액이 상환 금액보다 적습니다.',sleep = 1)
                                        clear()
                                        continue
                                    else:
                                        money -= repayAmount
                                        totLoan -= repayAmount
                                        typrint(f'{repayAmount}원 상환이 완료되었습니다.\n현재 잔액: {money}원\n총 대출 금액: {totLoan}원')
                                        break
                            if loanChoice in ['1', '대출받기']:
                                while True:
                                    loanAmount = int(tyinput(f'현재 대출 한도: {loanLimit}원\n대출 금액을 입력하세요: '))
                                    if loanAmount <= 0:
                                        typrint('\n올바른 금액을 입력하세요.',sleep = 1)
                                        clear()
                                        continue
                                    elif loanAmount > loanLimit:
                                        typrint('\n대출 한도를 초과했습니다.',sleep = 1)
                                        clear()
                                        continue
                                    else:
                                        money += loanAmount
                                        totLoan += loanAmount
                                        typrint(f'{loanAmount}원 대출이 완료되었습니다.\n현재 잔액: {money}원\n총 대출 금액: {totLoan}원')
                                        break    
            elif inGame1 in ['2', '돈벌기']:
                while True:
                    clear()
                    makeMoney = tyinput('------돈벌기------\n1. 동전 뒤집기\n2. 문제풀기\n3. 돌아가기\n')
                    if makeMoney in ['3', '돌아가기']:
                        clear()
                        triDotText('\n 길거리로 돌아갑니다')
                        clear()
                        break
                    if makeMoney in ['2', '문제풀기']:
                        for i in range(2):
                            math.append(random.randint(1,20))
                        a = math[0]
                        b = math[1]
                        guessNum = tyinput(f'다음 방정식의 근의 합을 A, 근의 곱을 B라고 할 때, AB 의 값은?\nx²+{a}x+{b}\n답: ')
                        if guessNum == str(-a*b):
                            money += 1000
                            typrint(f'정답입니다! {money}원 +1000원')
                        while True:
                            retry = tyinput('다시 하시겠습니까? (Y/N) : ')
                            if retry in ['Y', 'y']:
                                clear()
                                triDotText('\n 다음 문제')
                                clear()
                                break
                            elif retry in ['N', 'n']:
                                clear()
                                triDotText('\n 돈벌기로 돌아갑니다')
                                clear()
                                break
                            elif retry not in ['Y', 'y', 'N', 'n']:
                                clear()
                                typrint('Y or N 을(를) 입력하세요.',sleep = 1)
                                clear()
                                continue
                        clear()
                    if makeMoney in ['1', '동전 뒤집기']:
                        clear()
                        while True:
                            clear()
                            gueFlipcoin = tyinput('맞춰보세요! 앞/뒤 : ')
                            ansFlipcoin = 앞뒤[random.randint(0,1)]
                            if gueFlipcoin in ['앞', '뒤']:    
                                for i in range(15):
                                    time.sleep(0.05)
                                    clear()
                                    typrint(f'\n     {앞뒤1[i%2]}\n', sleep = 0 + (1/50)*i, delay = 0)
                                time.sleep(0.05)
                                clear()
                                typrint(f'\n     {앞뒤1[앞뒤.index(ansFlipcoin)]}\n', delay = 0)
                            elif gueFlipcoin == 앞뒤1[앞뒤.index(ansFlipcoin)]:
                                money += 500
                                typrint(f'{앞뒤[앞뒤.index(ansFlipcoin)]}면 정답입니다! {money}원 +500원')
                            else:
                                typrint(f'틀렸습니다! 정답은 {ansFlipcoin}면이었습니다.')
                            makeMoneyRetry = tyinput('다시 하시겠습니까? (Y/N) : ')
                            while True:    
                                if makeMoneyRetry in ['Y', 'y']:
                                    clear()
                                    triDotText('\n 동전을 다시 던집니다')
                                    clear()
                                    break
                                elif makeMoneyRetry in ['N', 'n']:
                                    clear()
                                    triDotText('\n 길거리로 돌아갑니다')
                                    clear()
                                    break
                                elif makeMoneyRetry not in ['Y', 'y', 'N', 'n']:
                                    clear()
                                    typrint('Y or N 을(를) 입력하세요.',sleep = 1)
                                    clear()
                                    continue
                            if makeMoneyRetry in ['Y', 'y']:
                                continue
                            elif makeMoneyRetry in ['N', 'n']:
                                break
            elif inGame1 in ['1', '임사장 카지노']:
                if usercoin <= 0:
                    typrint('코인이 부족합니다. 먼저 임금은행에서 환전을 해주세요.')
                    continue
                else:    
                    clear()
                    while True:
                        userbetmoney = int(tyinput(f'------임사장 카지노------\n현재 금액: {money}원\n베팅 코인을 입력하세요. : '))
                        if userbetmoney <= 0:
                            if count > 3:
                                typrint('얼른 나가지 못할까!!')
                                break
                            typrint(nomoney[count])
                            count += 1
                            continue
                        elif userbetmoney > money:
                            typrint('금액이 쪼달린다 닝겐')
                            continue
                        elif userbetmoney % 1000 != 0:
                            typrint('1000원 단위로만 걸도록 미천한 것.')
                            continue
                        else:
                            userbetcoin = userbetmoney//1000
                            money -= userbetmoney
                            typrint(f'{userbetmoney//1000}코인이 환전되었습니다.')
                            while True:
                                slot = slotIcon[random.randint(0,7)]
                                for i in range(15):
                                    time.sleep(0.05)
                                    clear()
                                    typrint(f'\n     ',sleep = 0, delay = 0, end = '')
                                    typrint(f'{slotIcon[i%8]} {slotIcon[(i+1)%8]} {slotIcon[(i+2)%8]}\n',sleep = 0 + (1/100)*i,delay = 0)
                                time.sleep(0.05)
                                clear()
                                typrint(f'\n     ',sleep = 0, delay = 0, end = '')
                                typrint(f'{slot}', delay = 0.5)
                                print(f'\n')
                                #------------------------#
                                if slot[0] == slot[1] == slot[2]:
                                    usercoin += userbetcoin * 10
                                    typrint(f'축하합니다! ✨잭팟✨입니다!\n총 {userbetcoin*10}코인을 획득하셨습니다.')
                                elif slot[0] == slot[1] or slot[1] == slot[2] or slot[2] == slot[0]:
                                    usercoin += userbetcoin * 2
                                    typrint(f'2개 일치! 총 {userbetcoin*2}코인을 획득하셨습니다.')
                                else:
                                    usercoin = 0
                                    typrint(f'0개 일치! {userbetcoin+usercoin}코인을 잃으셨습니다.')
                                while True:
                                    retry = tyinput('다시 돌리시겠습니까? (Y/N) : ')
                                    if retry in ['Y', 'y'] and usercoin > 0:
                                        while True:
                                            userbetcoin = int(tyinput(f'\n현재 코인: {usercoin}\n베팅할 코인을 입력해주세요.'))
                                            if userbetcoin > usercoin:
                                                typrint('코인이 부족합니다.')
                                                continue
                                            elif userbetcoin != usercoin:
                                                break
                                        break
                                    elif retry in ['N', 'n']:
                                        while True:
                                            clear()
                                            reretry = tyinput('정말 그만두시겠습니까? (Y/N) : ')
                                            if reretry in ['Y', 'y']:
                                                clear()
                                                triDotText('\n 임사장 카지노로 돌아갑니다')
                                                clear()
                                                break
                                            elif reretry in ['N', 'n']:
                                                break
                                            elif reretry not in ['Y', 'y', 'N', 'n']:
                                                typrint('Y or N 을(를) 입력하세요.')
                                                continue
                                        if reretry in ['Y', 'y']:
                                            break
                                        elif reretry in ['N', 'n']:
                                            continue
                                    elif usercoin <= 0:
                                        typrint('코인이 부족합니다. 임금은행에서 대출을 받거나 돈벌기를 이용해 주세요.')
                                        clear()
                                        triDotText('\n 길거리로 돌아갑니다')
                                        clear()
                                        break
                                    elif retry not in ['Y', 'y', 'N', 'n']:
                                        typrint('Y or N 을(를) 입력하세요.')
                                        continue
                                break
                            break
                continue

typrint(f'\n게임 오버~ {money}원 남았다~')