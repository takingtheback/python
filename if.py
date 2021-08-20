'''
조건문 java 의 switch문이 없음
괄호와 중괄호가 없음
if 조건:
    print('a')  # tab 키로 들여쓴 항목이 조건문 내용
    print('d')

줄이 안맞으면 오류남
 print('d') # <- if 문이랑 상관없는 구문


a = 10
if a>5:
    print('5보다 큼')
else:
    print('5보다 크지않음')

print('if 문구 벗어남')

a = 9
if a%2==1:
    print('a는 홀수')
else:
    print('a는 짝수')


if 조건:
    실행문
elif 조건:
    실행문
elif 조건:
    실행문
else:
    실행문    

import sys
score = 109

# Invalid 항목 처리
if score > 100 or score <0:
    print('올바르지 않은 점수입니다.')
    sys.exit(0) # 프로그램 종료

if score >= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score >= 70:
    print('C학점')
elif score >= 60:
    print('D학점')
else:
    print('F학점')

# 80 < score < 90 가능


# 반복문 java for each
for i in [1, 2, 3]:     # 1,2,3
    print(i)

for i in range(0, 5):   # 0,1,2,3,4 / range(시작숫자, 마지막숫자, 간격=1)
    print(i)

for i in range(0, 10):   # 0,1,2,3,...,9 / range(시작숫자, 마지막숫자, 간격=1)
    print(i)

for i in range(0, 10, 2):   # 0,2,4,6,8 / range(시작숫자, 마지막숫자, 간격=2)
    print(i)


for i in 'test text':
    print(i)

for i in range(1, 10):  # 1부터 9까지
    print(f'5 x {i} = {5*i}')

dan = 5
for i in range(1,10):
    print(dan,'*',i,'=',(dan*i))


while 조건:
    실행문

true 일동안 실행 false 되면 실행중지


i = 5
while i > 0:
    print(i)
    i -= 1  # i = 1 이 되면 무한 반복에 빠짐


# 형변환 함수
    int('123')
    float(12)=> 12.0
    flaot('23.345') => 23.345
    str(12) => '12'


while True:
    flag = input('멈추려면 0 입력 > ')   # 입력함수. 기본적으로 문자열로 입력받음
    if flag == '0':
        break   # 루프 빠져나감

    num = int(input('숫자를 입력하라 > '))
    print('입력한 숫자: ', num)

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

hp = 30
exp = 0
lv = 1
while True:
    menu = int(input('1. 밥먹기 2. 잠자기 3. 운동하기 4. 놀기 5. 상태확인 6. 종료 > '))
    if menu == 1:
        print('피카츄가 밥을 먹고, hp 가 5 회복되었다.')
        hp = hp + 5
        if hp > 30:
            hp = 30
        print('피카츄 lv: ',lv, ', hp: ',hp, ', exp: ',exp)
    if menu == 2:
        print('피카츄 잠을 자고, hp 가 10 회복되었다.')
        hp = hp + 10
        if hp > 30:
            hp = 30
        print('피카츄 lv: ', lv, ', hp: ', hp, ', exp: ', exp)
    if menu == 3:
        print('피카츄가 운동을 하고, hp 가 15 감소되었다.')
        print('exp 를 10 획득하였다.')
        hp = hp - 15
        exp = exp + 10
        print('피카츄 lv: ', lv, ', hp: ', hp, ', exp: ', exp)
        if hp <= 0:
            print('피카츄가 죽었다. 시스템을 종료합니다.')
            sys.exit(0)

        if exp >= 30:
            lv = lv + 1
            exp= exp - 30
            print('피카츄 레벨업!',' 레벨이',lv,'가 되었다.')

    if menu == 4:
        print('피카츄가 놀러가서, hp 가 10 감소되었다.')
        print('exp 를 5 획득하였다.')
        hp = hp - 10
        exp = exp + 5
        print('피카츄 lv: ', lv, ', hp: ', hp, ', exp: ', exp)

        if hp <= 0:
            print('피카츄가 죽었다. 시스템을 종료합니다.')
            sys.exit(0)

        if exp >= 30:
            lv = lv + 1
            exp= exp - 30
            print('피카츄 레벨업!',' 레벨이',lv,'가 되었다.')

    if menu == 5:
        print('피카츄 상태')
        print('lv', lv)
        print('hp',hp)
        print('exp',exp)

    if menu == 6:
        sys.exit(0)