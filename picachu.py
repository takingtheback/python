'''
포켓몬
피카츄
hp = 30
exp = 0
lv = 1

메뉴
1 밥먹기 > 피카츄 밥먹음. hp 5 증가
2 잠자기 > 피카츄 잠. hp 10 증가
3 운동하기 > 피카츄 운동함. hp -15 감소 exp 10 증가
4 놀기 > 피카츄 놀러감. hp -10 감소 exp 5 증가
5 상태확인 > hp exp lv
6 종료 >  sys.exit(0)

lv : exp 30 마다 1 증가
hp가 0 이하이면 케릭터 사망 : 게임종료

'''

import sys
name = 'picachu'
hp = 30
exp = 0
lv = 1
while True:
    menu = int(input('1. 밥먹기 2. 잠자기 3. 운동하기 4. 놀기 5. 상태확인 6. 종료 > '))
    if menu == 1:
        print(name,'가 밥을 먹고, hp 가 5 회복되었다.')
        hp += 5
        if hp > 30:
            hp = 30
        print(name,'lv: ',lv, ', hp: ',hp, ', exp: ',exp)

    elif menu == 2:
        print(name,'가 잠을 자고, hp 가 10 회복되었다.')
        hp += 10
        if hp > 30:
            hp = 30
        print(name,'lv: ', lv, ', hp: ', hp, ', exp: ', exp)

    elif menu == 3:
        print(name,'가 운동을 하고, hp 가 15 감소되었다.')
        print('exp 를 10 획득하였다.')
        hp -= 15
        exp = exp + 10
        print(name,'lv: ', lv, ', hp: ', hp, ', exp: ', exp)
        if hp <= 0:
            print(name,'가 죽었다. 시스템을 종료합니다.')
            break

        if exp >= 30:
            lv += 1
            exp= exp - 30
            print(name,'레벨업!',' 레벨이',lv,'가 되었다.')

    elif menu == 4:
        print(name,'가 놀러가서, hp 가 10 감소되었다.')
        print('exp 를 5 획득하였다.')
        hp -= 10
        exp += 5
        print(name,'lv: ', lv, ', hp: ', hp, ', exp: ', exp)

        if hp <= 0:
            print(name,'가 죽었다. 시스템을 종료합니다.')
            break

        if exp >= 30:
            lv += 1
            exp= exp - 30
            print(name,'레벨업!',' 레벨이',lv,'가 되었다.')

    elif menu == 5:
        print(name,'상태')
        print('lv', lv)
        print('hp',hp)
        print('exp',exp)

    elif menu == 6:
        print(name,'종료')
        sys.exit(0)
        break