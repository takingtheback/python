# 함수 정의
def my_input():
    name = input('name:')
    age = int(input('age:'))
    dept = input('dept:')
    return name, age, dept
    # 튜플형태로 (name, age, dept) 반환됨

# __name__ 속성 정보 : 모듈 이름
# def main():  으로 작성해도 가능 대신 main() 호출을 까먹지 말고 해야함
# if __name__ == '__main__': 프로그램의 시작점(main() 함수와 동일)
if __name__ == '__main__':
    data = my_input()
    print('name:', data[0])
    print('age:', data[1])
    print('dept:', data[2])

    name, age, dept = my_input()
    print('name:', name)
    print('age:', age)
    print('dept:', dept)

    name, age, _ = my_input() # 3개중에 2개만 필요한 경우우    print('name:', name)
    print('age:', age)
