"""
재귀함수 recursive function
함수 안에서 자신을 호출하는 함수
보통 반복 연산에 많이 사용됨
스택 사용량이 늘어나서 속도가 느려지거나 멈출 수 있음
가능하면 루프나 리스트 등으로 대체하는 것이 좋음

5! = 5*4*3*2*1
- 잘못사용하면 stack overflow 로 다운될 수 있음

"""

"""
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


result = fact(4)
print('fact(4):', result)


def fact2(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res


res = fact2(4)
print('fact2(4):', res)

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 2) + fibonacci(n - 1))

for i in range(1, 10):
    print(fibonacci(i), end=', ')


# 강사님 코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-2) + fibo(x-1)

for i in range(1,41):
    print(fibo(i), end=', ')
    if i%10 == 0:
        print()



def fibo2():
    x=y=z=1
    print(x, ',', y,end=', ')
    for i in range(3,20):
        if i < 3:
            z = 1
        else:
            z = x + y

        print(z, end=', ')
        x = y
        y = z

        if i%10 == 0:
            print()

fibo2()
"""


def fibo3(cnt):
    nums = [1]*cnt
    for i in range(2, len(nums)):
        nums[i] = nums[i-2] + nums[i-1]

    return nums

res = fibo3(20)
print(res)
