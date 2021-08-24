# 함수의 파라메터에 mutable한 값을 전달하면 함수에서 값을 변경하면 함수 밖에도 영향을 준다.
# 참조값으로 그 메모리에 직접 접근해서 값을 변경하기 때문

def f1(nums):
    print('함수에서 변경 전')
    for i in nums:
        print(i, end=', ')
    print()

    for i in range(0, len(nums)):
        nums[i] = nums[i]*10

    print('함수에서 변경 후')
    for i in nums:
        print(i, end=', ')
    print()


if __name__ == '__main__':
    n = [1, 2, 3, 4, 5]
    f1(n)
    print('main에서 함수 호출 후')
    for i in n:
        print(i, end=', ')
    print()
