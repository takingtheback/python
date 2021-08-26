"""
예외처리
컴파일시 에러 : 문법적 에러
예외 : 런타임시 문제 발생

# 예외발생
예외발생 -> 파이썬 시스템이 예외 객체를 생성해서 던진다 -> 프로그램이 예외객체를 맞으면 죽음

# 예외처리
- 프로그램이 예외객체를 맞았을 때 죽지 않게 처리
- 파이썬에서 예외처리가 필수는 아니지만 프로그램의 안정성을 높이기 위해서 사용하는 것이 좋음
"""

print('start')
arr = []
try:  # 예외가 발생할 수 있는 코드를 포함한 블록
    # a = 3/0
    # b = '1' + 2
    # print(a)
    # print(b)
    arr[0] = 1

except ZeroDivisionError:  # try 블록에서 던진 예외 객체를 받는 블록, 지정한 예외 객체만 받음
    print('ZeroDivisionError : 0으로 나눌 수 없음')

except TypeError as e:  # try 블록에서 던진 예외 객체를 받는 블록, 지정한 예외 객체만 받음
    print('TypeError : 피연산자들의 타입 불일치')
    # print(e.__str__())  # java toString 동일
    print(e)
except Exception as ae:
    print('모든 에러')
    print(ae)
else:
    print('예외없이 정상 실행')
finally:
    print('예외 발생 유무와 상관없이 무조건 실행')

print('end')

