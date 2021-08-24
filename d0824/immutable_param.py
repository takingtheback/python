# 함수의 파라메터가 immutable인 값을 받을 때 함수에서 값을 수정하면 어떻게 되는가?
# immutable한 값을 파라메터로 전달하여 함수에서 변경하더라도 원본에는 영향이 가지 않는다.
def f1(num, name, tu):
    print('함수에서 수정 전')
    print('num', num)
    print('name', name)
    print('tu', tu)
    num = 100
    name = 'kkk'
    tu = (5, 6, 7, 8)

    print('함수에서 수정 후')
    print('num', num)
    print('name', name)
    print('tu', tu)


if __name__ == '__main__':
    n = 10
    name = 'aaa'
    t = (1, 2, 3)
    f1(n, name, t)
    print('main에서 함수 호출 후')
    print('num', n)
    print('name', name)
    print('tu', t)
