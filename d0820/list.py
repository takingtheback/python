'''
리스트 : java의 배열. 집합데이터를 편하게 사용
변수정의: 값을 저장하기 위해 메모리를 할당받음
# java
int[] a = {1, 2, 3};

# 1. 리스트 생성
a = [1, 2, 3]
b = list(a)
c = list([4, 5, 6])
d = list()

# 2. 요소 접근
a[0]
a[1]
a[2]
# a[3] => Error

# for문 이용한 접근
for i in range(0, len(a)):
    print(a[i])

# 더 많이 사용되는 표현
for i in a: #[1, 2, 3]
    print(i)


a = [1, 2, 3, 4, 5]
for i in a:
    print(i, end=', ')


# 한 리스트에 여러 타입의 값 저장 가능
b = [1, 2.345, 'text', True]
for i in b:
    print(i)

c = list(range(1, 6))
print(c)


# 3. 요소 추가
a = [1, 2, 3]
# a[3] = 4 Error
print(len(a))
print(a)
a.append(4)
print(len(a))
print(a)

# 4. 요소 수정
a[0] = 123
a[1] = 456
print(a)

# 5. 요소 삭제
del a[0] # 방번호로 삭제
print(a)
print(len(a))

a.remove(3) # 요소를 삭제, 없는 값 삭제시 ValueError: list.remove(x): x not in list
print(a)
print(len(a))

# 6. 전체 삭제
a.clear()
print(a)

실습
정수 10개를 input() 으로 입력받아서 리스트에 저장
리스트에서 최대값 최소값 찾아서 출력


a = []
for i in range(0, 10):
    num = int(input('num : '))
    a.append(num)
print(a)

max_value = None
for num in a:
    if (max_value is None or num > max_value):
        max_value = num

print('Maximum value:', max_value)

min_value = None
for num in a:
    if (min_value is None or num < min_value):
        min_value = num

print('Minimum value:', min_value)


a = []
for i in range(0, 10):
    num = int(input('num : '))
    a.append(num)
print(a)

# _max : 가장 큰 값을 담을 변수
# _min : 가장 작은 값을 담을 변수
_max = _min = a[0]

# enumerate : 반복자 = 방번호까지 알려줌
for idx, i in enumerate(a):
    if _max < i:
        _max = i
        max_idx = idx

    if _min > i:
        _min = i
        min_idx = idx

print('max: ', _max, ' / max_idx: ', max_idx)
print('min: ', _min, ' / min_idx: ', min_idx)


# 7. 요소 검색
in : 멤버 연산자. 왼쪽의 값이 오른쪽 리스트의 요소인지 True, False로 반환



a = [1, 2, 3, 4, 5]
print(3 in a)
print(6 in a)

if 3 in a:
    print('3은 리스트 a의 멤버가 맞다')
    print(a.index(3),'번째 방에 있음')

# print(a.index(7)) => 없는 값 Error


# 요소 정렬
b = [7,3,9,4,6]
b.sort()
print(b)

b.sort(reverse=True)
print(b)


# 2차원 리스트

a = [[1, 2, 3], [4, 5, 6]]
for i in a:
    for j in i: # [1, 2, 3]
        print(j, end=', ')
    print()

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=', ')
    print()

b = [['aaa', 1, True, 34.567], [23, False]]
for i in b:
    for j in i:
        print(j, end=', ')
    print()
'''

