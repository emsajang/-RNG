# 라이브러리
import random
import time
import os

# 변수
loanLimit = 100000
bankBalance = 100000000
bankCoin = 100000
money = 5000
speed = 0.05
totLoan = 0
count = 0
userCoin = 0
fxa = 0
fxb = 0
n1 = 0
n2 = 0
n3 = 0

# 리스트
tip = ['오타나면 타입에러가 뜰 수 있으니 조심하세요!','게임이 종료되면 모든 진행 상황을 잃습니다.','메인메뉴 - 설정에서 대사속도를 바꾸실 수 있어요.','제작자: 임사장','수업시간에 배운 파이썬 코드를 기반으로 만들었습니다.','주인공은 아무런 직업도 없답니다.','과거 분수대에 총 100,000코인을 던진 한 남자가 신이 됐다는 마을 전설이...','동전 뒤집기보다 수학 문제가 돈을 더 많이 준답니다~','이거 만드는 데 6시간은 걸렸대요.']
slot = ['slot1','slot2','slot3']
math = [0,0]
nomoney = ['경고 1회','경고 2회','경고 3회','경비원이 다가옵니다..']
slotIcon = ['🍋','🍒','🍓','🍇','⭐️','💎','🍀','💰']
앞뒷 = ['앞', '뒷']
앞뒤 = ['앞', '뒤']

# typrint
def typrint(text, sleep=float(0.25), delay = None, end = None, sep = None):
    if delay is None:
        delay = float(speed)
    
    if end is None:
        end = '\n'
    
    if sep is None:
        sep = ' '

    for chat in text:
        print(chat, end='', flush=True, sep = sep)
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
    print(f'\n\n\n *Tip: {tip[random.randint(0,len(tip)-1)]}',end = '')
    print('\r\033[2A',end = '')
    typrint(f' {text}',end = '')
    typrint('...', delay = 0.75, end = '')

# onlytriDotText
def onlytriDotText(text):
    typrint(f' {text}',end = '')
    typrint('...', delay = 0.75, end = '')


#---MainGame---#
clear()
time.sleep(0.5)
while True: # 시작화면
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
                        onlytriDotText(f'대출 한도가 {loanLimit}원으로 설정되었습니다')
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
                        onlytriDotText(f'대사 속도가 {speed}으로 설정되었습니다')
                        clear()
                        continue
                    elif settingSpeed in ['3', '느리게']:
                        clear()
                        speed = 0.1
                        onlytriDotText(f'대사 속도가 {'느리게'}로 설정되었습니다')
                        clear()
                        continue
                    elif settingSpeed in ['2', '보통']:
                        clear()
                        speed = 0.05
                        onlytriDotText(f'대사 속도가 {'보통'}으로 설정되었습니다')
                        clear()
                        continue
                    elif settingSpeed in ['1', '빠르게']:
                        clear()
                        speed = 0.0075
                        onlytriDotText(f'대사 속도가 {'빠르게'}로 설정되었습니다')
                        clear()
                        continue
                if settings not in ['1', '2', '3', '대사 속도', '대출 한도', '돌아가기']:
                    clear()
                    typrint('잘못된 선택입니다.',sleep = 1)
                    clear()
                    continue
    elif mainMenu in ['1', '게임시작']:
        clear()
        triDotText(f'고작 {money}원만 가진 채 길거리로 떠납니다')
        while True: # --메인메뉴--
            if userCoin >= 100000:
                goEnd = tyinput('100,000코인을 모으셨습니다.\n분수대에 던지시겠습니까? Y/N : ')
                if goEnd in ['Y','y']:
                    break#추가예정 어짜피 10만코인 못 모음
                elif goEnd in ['N','n']:
                    break#추가예정 어짜피 10만코인 못 모음
            clear()
            inGame1 = tyinput('------길거리------\n1. 임사장 카지노\n2. 돈벌기\n3. 임금은행\n4. 통계 - 만드는중\n5. 돌아가기\n')
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
            elif inGame1 in ['3', '임금은행']:
                clear()
                triDotText('임금은행으로 이동합니다')
                clear()
                while True:    
                    clear()
                    bankChoice = tyinput('------임금은행------\n1. 대출\n2. 환전\n3. 대출 정보\n4. 돌아가기\n')
                    if bankChoice in ['4', '돌아가기']:
                        clear()
                        triDotText('길거리로 돌아갑니다')
                        clear()
                        break
                    elif bankChoice in ['3', '대출 정보']:
                        clear()
                        typrint(f'------대출정보------\n금리: 10%\n현재 대출 한도: {loanLimit}원\n총 대출 금액: {totLoan}원')
                        onlytriDotText('')
                    elif bankChoice in ['2', '환전']:
                        while True:
                            clear()
                            exchangeChoice = tyinput('------환전------\n1. 코인 -> 현금\n2. 현금 -> 코인\n3. 돌아가기\n')
                            if exchangeChoice in ['3', '돌아가기']:
                                break
                            elif exchangeChoice in ['2','현금 -> 코인']:
                                if money == 0:
                                    clear()
                                    typrint('현금이 부족합니다.')
                                    clear()
                                    continue
                                while True:
                                    clear()
                                    exchangeAmount = int(tyinput(f'[1000원 -> 1코인]\n현재 잔액: {money}원\n환전할 금액을 입력하세요: '))
                                    if exchangeAmount <= 0:
                                        clear()
                                        typrint('올바른 금액을 입력하세요.',sleep = 1)
                                        clear()
                                        continue
                                    elif exchangeAmount % 1000 != 0:
                                        clear()
                                        typrint('1000원 단위로만 환전이 가능합니다.',sleep = 1)
                                        clear()
                                        continue
                                    elif exchangeAmount > money:
                                        clear()
                                        typrint('환전 금액이 보유한 코인보다 많습니다.')
                                        clear()
                                        continue
                                    else:
                                        clear()
                                        money -= exchangeAmount
                                        bankBalance += exchangeAmount
                                        userCoin += exchangeAmount//1000
                                        bankCoin -= exchangeAmount//1000
                                        typrint(f'{exchangeAmount}원이 환전 되었습니다.\n현재 코인: {userCoin}코인')
                                        onlytriDotText('')
                                        clear()
                                        break
                            elif exchangeChoice in ['1','코인 -> 현금']:
                                if userCoin == 0:
                                    clear()
                                    typrint('코인이 부족합니다.')
                                    clear()
                                    continue
                                while True:
                                    clear()
                                    exchangeAmount = int(tyinput(f'[1코인 -> 900원]\n현재 코인: {userCoin}코인\n환전할 코인을 입력하세요: '))
                                    if exchangeAmount <= 0:
                                        clear()
                                        typrint('올바른 수량을 입력하세요.',sleep = 1)
                                        clear()
                                        continue
                                    elif exchangeAmount > userCoin:
                                        clear()
                                        typrint('코인이 부족합니다.')
                                        clear()
                                        continue
                                    else:
                                        clear()
                                        userCoin -= exchangeAmount
                                        bankCoin += exchangeAmount
                                        money += exchangeAmount*900
                                        bankBalance -= exchangeAmount*900
                                        typrint(f'{exchangeAmount}코인이 환전 되었습니다.\n현재 잔액: {money}원')
                                        onlytriDotText('')
                                        clear()
                                        break
                    elif bankChoice in ['1', '대출']:
                        while True:
                            clear()
                            loanChoice = tyinput('------대출------\n1. 대출받기\n2. 대출갚기\n3. 돌아가기\n')
                            if loanChoice in ['3', '돌아가기']:
                                clear()
                                break
                            if loanChoice in ['2', '대출갚기']:
                                if totLoan == 0:
                                    clear()
                                    typrint('부채가 없습니다.')
                                    clear()
                                    continue
                                while True:
                                    clear()
                                    repayAmount = int(tyinput(f'현재 대출 금액: {totLoan+totLoan*0.1}원(이자 포함됨.)\n갚을 금액을 입력하세요: '))
                                    clear()
                                    if repayAmount <= 0:
                                        typrint('\n올바른 금액을 입력하세요.',sleep = 1)
                                        clear()
                                        continue
                                    elif repayAmount > totLoan + totLoan*0.1:
                                        typrint('\n갚을 금액이 대출 금액보다 많습니다.',sleep = 1)
                                        clear()
                                        continue
                                    elif repayAmount > money:
                                        typrint('\n보유한 금액이 갚을 금액보다 적습니다.',sleep = 1)
                                        clear()
                                        continue
                                    else:
                                        money -= repayAmount
                                        totLoan -= repayAmount - totLoan*0.1
                                        bankBalance += repayAmount
                                        typrint(f'{repayAmount}원을 갚았습니다.\n현재 잔액: {money}원\n총 대출 금액: {totLoan}원')
                                        break
                            if loanChoice in ['1', '대출받기']:
                                if totLoan == loanLimit:
                                    clear()
                                    typrint('한도 초과입니다.')
                                    clear()
                                    continue
                                while True:
                                    clear()
                                    loanAmount = int(tyinput(f'현재 금리: 10%\n현재 대출 한도: {loanLimit}원\n대출 금액을 입력하세요: '))
                                    if loanAmount <= 0:
                                        clear()
                                        typrint('\n올바른 금액을 입력하세요.',sleep = 1)
                                        clear()
                                        continue
                                    elif totLoan + loanAmount > loanLimit:
                                        clear()
                                        typrint('\n대출 한도를 초과했습니다.',sleep = 1)
                                        clear()
                                        continue
                                    else:
                                        clear()
                                        money += loanAmount
                                        totLoan += loanAmount
                                        bankBalance -= loanAmount
                                        typrint(f'{loanAmount}원이 대출 완료되었습니다.\n현재 잔액: {money}원\n총 대출 금액: {totLoan}원')
                                        onlytriDotText('')
                                        clear()
                                        break    
            elif inGame1 in ['2', '돈벌기']:
                while True:
                    clear()
                    makeMoney = tyinput('------돈벌기------\n1. 동전 뒤집기\n2. 문제풀기\n3. 돌아가기\n')
                    if makeMoney in ['3', '돌아가기']:
                        clear()
                        triDotText('길거리로 돌아갑니다')
                        clear()
                        break
                    if makeMoney in ['2', '문제풀기']:
                        while True:    
                            for iMath in range(2):
                                math[iMath] = random.randint(-20,20)
                            fxa = math[0] 
                            fxb = math[1]
                            clear()
                            guessNum = int(tyinput(f'다음 방정식의 근의 합을 A, 근의 곱을 B라고 할 때, AB 의 값은?\nx²+{fxa}x+{fxb}\n답: '))
                            if guessNum == -fxa*fxb:
                                money += 1000
                                typrint(f'[ {guessNum} ] 정답입니다! {money}원 +1000원')
                            else:
                                typrint(f'{guessNum} 틀렸습니다! 정답은 {-fxa*fxb} 입니다.')
                            while True:
                                mathRetry = tyinput('다시 하시겠습니까? (Y/N) : ')
                                if mathRetry in ['Y', 'y']:
                                    clear()
                                    onlytriDotText('다음 문제')
                                    clear()
                                    break
                                elif mathRetry in ['N', 'n']:
                                    clear()
                                    triDotText('돈벌기로 돌아갑니다')
                                    clear()
                                    break
                                elif mathRetry not in ['Y', 'y', 'N', 'n']:
                                    clear()
                                    typrint('Y or N 을(를) 입력하세요.',sleep = 1)
                                    clear()
                                    continue
                            if mathRetry in ['Y','y']:
                                continue
                            elif mathRetry in ['N','n']:
                                break
                        clear()
                    if makeMoney in ['1', '동전 뒤집기']:
                        clear()
                        while True:
                            clear()
                            gueFlipcoin = tyinput('맞춰보세요! 앞/뒤 : ')
                            ansFlipcoin = 앞뒷[random.randint(0,1)]
                            if gueFlipcoin in ['앞', '뒤']:    
                                for i in range(15):
                                    time.sleep(0.05)
                                    clear()
                                    typrint(f'\n     {앞뒤[i%2]}\n', sleep = 0 + (1/50)*i, delay = 0)
                                time.sleep(0.05)
                                clear()
                                typrint(f'\n     {앞뒤[앞뒷.index(ansFlipcoin)]}\n', delay = 0)
                            elif gueFlipcoin == f'{앞뒤[앞뒷.index(ansFlipcoin)]}':
                                money += 500
                                typrint(f'{앞뒷[앞뒷.index(ansFlipcoin)]}면 정답입니다! {money-500}원 +500원')
                            else:
                                typrint(f'틀렸습니다! 정답은 {ansFlipcoin}면이었습니다.')
                            makeMoneyRetry = tyinput('다시 하시겠습니까? (Y/N) : ')
                            while True:    
                                if makeMoneyRetry in ['Y', 'y']:
                                    clear()
                                    onlytriDotText('동전을 다시 던집니다')
                                    clear()
                                    break
                                elif makeMoneyRetry in ['N', 'n']:
                                    clear()
                                    triDotText('돈벌기로 돌아갑니다')
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
                if userCoin == 0:
                    clear()
                    typrint('코인이 부족합니다. 먼저 임금은행에서 환전을 해주세요.')
                    clear()
                    continue
                else:
                    clear()
                    while True:
                        userbetcoin = int(tyinput(f'------임사장 카지노------\n현재 코인: {userCoin}코인\n베팅 코인을 입력하세요. : '))
                        if userbetcoin <= 0:
                            if count > 3:
                                clear()
                                typrint('얼른 나가지 못할까!!')
                                onlytriDotText('길거리로 내쫓겼다')
                                clear()
                                break
                            typrint(nomoney[count])
                            count += 1
                            continue
                        elif userbetcoin <= userCoin:
                            userCoin -= userbetcoin
                            while True:
                                # 슬롯 채워넣기
                                for ranSlot in range(3):    
                                    slot[ranSlot] = slotIcon[random.randrange(len(slotIcon))]
                                # 슬롯 돌리기
                                for i in range(15):
                                    time.sleep(0.05)
                                    clear()
                                    typrint(f'\n     ',sleep = 0, delay = 0, end = '')
                                    typrint(f'⟪{slotIcon[i%8]}⟫⟪{slotIcon[(i+1)%8]}⟫⟪{slotIcon[(i+2)%8]}⟫\n',sleep = 0 + (1/100)*i,delay = 0)
                                time.sleep(0.05)
                                clear()
                                # 결과 띄우기
                                typrint(f'\n     ',sleep = 0, delay = 0, end = '')
                                typrint(f'⟪{'⟫⟪'.join(slot)}⟫', delay = 0.5//3) # 결과
                                print(f'\n')
                                # 결과 판단하고 돈 추가하기
                                if slot[0] == slot[1] == slot[2]:
                                    userCoin += userbetcoin * 10
                                    typrint(f'축하합니다! ✨잭팟✨입니다!\n총 {userbetcoin*10}코인을 획득하셨습니다.')
                                elif slot[0] == slot[1] or slot[1] == slot[2] or slot[2] == slot[0]:
                                    userCoin += userbetcoin * 2
                                    typrint(f'2개 일치! 총 {userbetcoin*2}코인을 획득하셨습니다.')
                                else:
                                    userCoin = 0
                                    typrint(f'0개 일치! {userbetcoin+userCoin}코인을 잃으셨습니다.')
                                while True:
                                    retry = tyinput('다시 돌리시겠습니까? (Y/N) : ')
                                    if retry in ['Y', 'y'] and userCoin > 0:
                                        while True:
                                            if userCoin <= 0:
                                                typrint('코인이 부족합니다.')
                                                userbetcoin = 0
                                                break
                                            userbetcoin = int(tyinput(f'\n현재 코인: {userCoin}\n베팅할 코인을 입력해주세요.'))
                                            if userbetcoin > userCoin:
                                                typrint('코인이 부족합니다.')
                                                continue
                                            elif userbetcoin <= userCoin:
                                                break
                                        break
                                    elif retry in ['N', 'n']:
                                        while True:
                                            clear()
                                            reretry = tyinput('정말 그만두시겠습니까? (Y/N) : ')
                                            if userCoin <= 0:
                                                userbetcoin = 0
                                            if reretry in ['Y', 'y']:
                                                clear()
                                                triDotText('임사장 카지노로 돌아갑니다')
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
                                    elif userCoin <= 0:
                                        typrint('코인이 부족합니다. 임금은행에서 대출을 받거나 돈벌기를 이용해 주세요.')
                                        clear()
                                        triDotText('길거리로 돌아갑니다')
                                        clear()
                                        break
                                    elif retry not in ['Y', 'y', 'N', 'n']:
                                        typrint('Y or N 을(를) 입력하세요.')
                                        continue
                                if reretry in ['Y','y']:
                                    break
                                elif reretry in ['N','n']:
                                    continue
                                break
                            if userbetcoin <= 0 or (retry in ['N', 'n'] and reretry in ['N', 'n']):
                                break
                            else:
                                continue
                            
                    break
            continue

typrint(f'\n게임 오버~ {money}원 남았다~')