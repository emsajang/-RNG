# 라이브러리
import random
import time

# 변수
count = 0
money = 5000
usercoin = 0
n1 = 0
n2 = 0
n3 = 0

# 리스트
nomoney = ['돈이 없음 썩 꺼지거라.','분명 말했다. 돈 없음 가라.','마지막 경고다. 돈이 없더냐? 그럼 나가라.','...']
slotIcon = ['🍋','🍒','🍓','🍇','⭐️','💎','🍀','💰']

# typrint
def typrint(text, slen=float(0.25), delay=float(0.05)):
    for chat in text:
        print(chat, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(slen)
# tyinput
def tyinput(prompt, delay=float(0.05)):
    for chat in prompt:
        print(chat, end="", flush=True)
        time.sleep(delay)
    return input()
# gameOver
def gameOver():
    typrint(f'최종 금액: {money}원',0.5)
    typrint('☠️ 게 임 오 버 ☠️',0.25,0.15)

# MainGame
time.sleep(1)
typrint('슬롯머신에 오신 것을 환영합니다.')
typrint('[1코인 = 1000원] 입니다.')
typrint('잭팟 - 10배')
typrint('2개 - 2배')
typrint('1개 - 0배')
while True:
    mainMenu = int(tyinput('------슬롯머신 게임------\n1. 게임시작\n2. 설정\n3. 제작자\n4. 종료\n'))
    if mainMenu == 4:
        gameOver()
        break
    if mainMenu == 3:
        typrint('Made by Ang임사장')
        continue
    if mainMenu == 2:#추가예정
        while True:
            print()
            
    if mainMenu == 1:
        while True:
            #슬롯머신, 은행, 돈벌기 메뉴 추가 예정
            while True:
                typrint(f'현재 금액: {money}원')
                userbetmoney = int(tyinput("베팅 금액을 입력하이소: "))
                if userbetmoney <= 0:
                    if count > 3:
                        typrint('얼른 나가지 못할까!!')
                        break
                    typrint(nomoney[count])
                    count += 1
                    continue
                if userbetmoney > money:
                    typrint('금액이 쪼달린다 닝겐')
                    continue
                if userbetmoney % 1000 != 0:
                    typrint('1000원 단위로만 걸도록 미천한 것.')
                    continue
                else:
                    userbetcoin = userbetmoney//1000
                    money -= userbetmoney
                    typrint(f'{userbetmoney//1000}코인이 환전되었습니다.')
                    while True:
                        slot1 = slotIcon[random.randint(0,7)]
                        slot2 = slotIcon[random.randint(0,7)]
                        slot3 = slotIcon[random.randint(0,7)]
                        #---인터페이스 추가 예정----#
                        typrint(f'{slot1} {slot2} {slot3}',0.25,0.5)
        
                        #------------------------#
                        if slot1 == slot2 == slot3:
                            usercoin += userbetcoin * 10
                            typrint(f'축하합니다! ✨잭팟✨입니다!\n총 {userbetcoin*10}코인을 획득하셨습니다.')
                        elif slot1 == slot2 or slot2 == slot3 or slot3 == slot1:
                            usercoin += userbetcoin * 2
                            typrint(f'2개 일치! 총 {userbetcoin*2}코인을 획득하셨습니다.')
                        else:
                            usercoin = 0
                            typrint(f'0개 일치! {userbetcoin+usercoin}코인을 잃으셨습니다.')
                        while True:
                            retry = tyinput('다시 돌리시겠습니까? Y/N ')
                            if retry == 'Y' and usercoin > 0:
                                while True:
                                    userbetcoin = int(tyinput(f'\n현재 코인: {usercoin}\n(남은 코인은 자동으로 환전됩니다.)\n베팅할 코인을 입력해주세요.'))
                                    if userbetcoin > usercoin:
                                        typrint('코인이 부족합니다.')
                                        continue
                                    else:
                                        money += (usercoin - userbetcoin)*1000
                                        typrint(f'{usercoin - userbetcoin}코인이 {(usercoin - userbetcoin)*1000}원으로 환전되었습니다.')
                                        break
                                break
                            elif retry == 'N':
                                reretry = tyinput('정말 그만두시겠습니까? Y/N ')
                                if reretry == 'Y':
                                    money += usercoin*1000
                                    usercoin = 0
                                    typrint(f'{usercoin*1000}원이 저장되었습니다.')
                                    break
                                elif reretry == 'N':
                                    continue
                            elif usercoin <= 0:
                                typrint('코인이 부족합니다. 은행에서 대출을 받으세요.')
                                break
                            else:
                                typrint('Y or N을 입력하세요.')
                        break
                    break
            break
        break

typrint(f'\n게임 오버~ {money}원 남았다~')