
try:
    num = int(input('5 이하의 숫자를 입력하시오.> '))
    if num > 5:
        raise ValueError('value error')     # 예외 발생
    print('입력값:', num)
except ValueError as e:
    print('5 이하의 값만 출력')
    print(e)
print('stop')

