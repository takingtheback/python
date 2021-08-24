# 요구 인자 : 함수 호출시 아규먼트의 개수와 순서가 맞아야함
def f1(name, tel, age):
    print('name:', name)
    print('tel:', tel)
    print('age:', age)


# f1('aaa', 12, '컴공')
# f1('aaa', '전차', 23) 부서 나이 순서 바뀌면서 에러 TypeError: can only concatenate str (not "int") to str
# 요구 인자 : 순서가 바뀌어도 작동
# f1(name='aaa', dept='전차', age=23)
# f1('aaa', 12) # TypeError: f1() missing 1 required positional argument: 'dept' 기본값이 없어서 오류
# f1('aaa', 12) # f1에 기본값 f1(name='aaa', age=0, dept='전자'): 를 설정했으므로 오류가 안남
# f1(age=23)

# 키워드 인자 : 각 아규먼트가 어느 파라메터로 전달될지 지정하므로 순서 바뀌어도 상관없음
def f2(name, tel, age):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age + 10)


# f2('111', 12 'aaa') 아규먼트의 순서가 안맞아서 에러
f2(tel='111', age=12, name='aaa')


# 디폴트 인자 : 아규먼트의 기본값을 지정하므로 함수 호출시 생략 가능함
def f3(name='aaa', tel='1234', age=10):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age + 10)


f3('bbb')
f3('ccc', 12)
f3(age=22)


# 디폴트 지정안된 값은 앞으로 와야함
# f4는 가능 f5는 불가
def f4(name, tel='1234', age=10):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age + 10)


'''
# 지정안된 값이 뒤에 혹은 가운데 있으면 에러가 발생 
- SyntaxError: non-default argument follows default argument
def f5(name='aaa', tel, age=10):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age + 10)
'''


# 가변인자 : 아규먼트의 개수가 가변, 튜플형태로 전달됨
def f6(*param):  # 가변인자, 튜플로 받아옴 param('aaa', 'bbb')
    print('함수시작')
    for i in param:
        print(i)
    print('함수끝')


f6()
f6('aaa')
f6('aaa', 'bbb', 'ccc')


# 모든 숫자의 합
def total(*param):
    result = 0
    for i in param:
        result += i

    print(result)


total(1, 2, 3, 4, 5)


# answer
def my_sum(*nums):
    res = 0
    for i in nums:
        res += i
    return res


print('파라메터 없음:', my_sum())
print('1,2,3:', my_sum(1, 2, 3))
print('1, 2, 3, 4, 5:', my_sum(1, 2, 3, 4, 5))


def memInfo(num, name, kor, eng, math):
    print('num', num)
    print('name', name)
    print('total', kor + eng + math)


data = [1, 'aaa', 65, 46, 54]
memInfo(*data)
