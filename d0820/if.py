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

break 문
루프 빠져나감

continue문
continue문 뒤의 문장을 실행하지 않고 다름 루프 진행
'''
# 1- 10 사이의 짝수 출력
for i in range(1, 11):
    if i%2 == 1:
        continue
    print(i, end=', ')  # end:출력시 마지막 출력값. 기본값은 \n
print()
for i in range(2, 11, 2):
    print(i, end=', ')
