'''
# 튜플
- 튜플 자체도 변경불가, 요소도 변경 불가
- 고정된 집합ㅇ느로 요소를 추가, 변경, 삭제가 안됨
- 값의 순서(인덱스)가 있음
- 활용: 함수의 값 주고 받을 때 값 변경을 허용하지 않을 때 사용

a = (1, 2, 3, 4, 5)
# a[0] = 10 # TypeError: 'tuple' object does not support item assignment
print(a)
# a = (1, 2, [3, 4, 5])
# a[2][0] = 10  # (1, 2, [10, 5, 6]) 우회하여 변경: 튜플 안에 배열 넣어 배열값을 변경하는 것은 가능
# img.shape=(h, w, c) 이미지 파일에 대한 사이즈 고정 가능

b=[1, 2, 3]
l = list() # 빈 리스트 l=[]
'''
'''
a = (1, 2, 3, 4, 5)
# t= tuple() # 빈 튜플 : 요소 추가가 어려워서 빈 튜플은 잘 쓰지 않음

print(a)

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])
    
# 초기화: 방 7개 0으로 초기화
t0 = [0]*7
t1 = (1,)*3
t2 = ('hello',)*5
print(t0)
print(t1)
print(t2)
'''
'''
x = (1, 2.345, 'text', True, [1, 2, 3])
print(x)
print(type(x))

a = (1, 2, 3, 4, 5)

b = ((1, 2, 3), {3, 4, 5})
for i in b:
    for j in i:
        print(j)

for i in range(-5, 0):
    print(a[i])
'''
'''
요소 슬라이싱
- 원본에 영향을 주지 않음

a = [1, 2, 3, 4, 5] # 리스트
b = (6, 7, 8, 9, 10) # 튜플
r1 = a[0:3] # a요소 0-2까지 (마지막숫자-1)
print(r1)
r2 = b[2:5] # b요소 2-4까지
print(r2)

# len() : 길이
# sum() : 리스트나 튜플 요소의 합
# max() : 최대값
# min() : 최소값

a_len = len(a)
print(a_len)

s1 = sum(a)
s2 = sum(b)
print(s1, '/', s2)

max_a = max(a)
max_b = max(b)
print(max_a, '/', max_b)
'''
'''
# 검색, 비교
# in : 멤버쉽 연산자, 집합에 비교하는 값이 있나, 없나를 True, False로 반환

a = [1, 2, 3, 4, 5] # 리스트
b = (6, 7, 8, 9, 10) # 튜플
print(3 in a)
print(13 in a)
print(3 not in a)
print(13 not in a)

print(3 in b)
print(10 in b)

c = (6, 11, 12, 13) # 중복된 값도 튜플에 들어감
x = b + c
print(x)
'''
'''
# int 변수가 3개 만들어짐
x, y, z = 1, 2, 3
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
'''
'''
t1 = 1, 2, 3
t2 = 3, 4, 5
t3 = 1, 2, 3

print(t1)
print(type(t1))

print(t2)
print(type(t2))

print(t3)
print(type(t3))

print(t1 != t2)
print(t1 == t3)
'''
'''
# 요소 추가, 삭제, 변경 안됨
'''
# a[3] = 4 # TypeError: 'tuple' object does not support item assignment
# a[0] = 4 # TypeError: 'tuple' object does not support item assignment
# 튜플은 요소에 = (대입연산자)를 사용할 수 없음
a = (1, 2, 3,[])
a[3].append(10)
a[3].append(20)
print(a)
del a[3][0]
print(a)