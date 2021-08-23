'''
# 함수
java method 역할 : function
# 함수 정의
    - 함수가 어떤 동작을 할 때 필요한 값, 그 값은 어떻게 받을지 정의

    def 함수명 (param1, param2):
        실행문
        return 결과값

# 함수 호출
    - 함수의 이름을 불러서 함수 실행
    - 파라메타가 있다면 값 전달(아규먼트)

    result = 함수명(10, 20)

'''
# 메인이 없어도 실행하는데 문제는 없다.
# 다만 가독성이 떨어지므로 if __name__ == '__main__': 를 사용해주면 좋다.
'''
# 함수 정의
def hello(name):
    print('hello', name)

# 함수 호출
hello('namaewa')
hello(10)
hello(3.14)

def add(num1, num2):
    return num1+num2

print(add(1, 2))
print(add('1', '2'))
# print(add(1, '2')) TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
'''
- 단수 1개를 파라메터로 받음
- 해당 단수를 구구단 출력

def gugudan(dan):
    print(dan,'단')
    for i in range(1,10):
        print(dan, '*', i, '=', dan*i)

for i in range(2,10):
    gugudan(i)
'''
# 함수 밖에 정의하고 모든 함수들이 사용할 수 있는 변수 : 전역변수
nums = []

# nums 항목 추가
def add_num(num):
    nums.append(num)

# nums 모든 요소 출력
def print_nums():
    for i in nums:
        print(i, end=', ')
    print()

# nums idx 항목을 num 으로 수정
def edit_num(idx, num):
    nums[idx] = num

def del_num(idx):
    del nums[idx]

# nums: [1, 2, 3, 4, 5]
for i in range(1,6):
    add_num(i)

print_nums()

edit_num(2,30)

print_nums()

del_num(2)

print_nums()