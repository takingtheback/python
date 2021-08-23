'''
# 얕은 복사
a = [1, 2, 3]
b = a # 얕은 복사
print(a)
print(b)

# java 참조값 복사 비슷
b[1] = 20
print(a)
print(b)

print(id(a))
print(id(b))
'''
'''
# 깊은 복사
import copy
a = [1, 2, 3]
b = copy.copy(a) # 깊은 복사1
print(a)
print(b)

print(id(a))
print(id(b))

b[1] = 20
print(a)
print(b)
'''
'''
import copy
a = [1, 2, [3, 4]]
b = copy.copy(a) # 참조값을 복사했기 때문에 a도 변경되는 상황 발생
print(a)
print(b)

print(id(a))
print(id(b))

b[2][0] = 300
print(a)
print(b)
'''
'''
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a) # 깊은 복사
print(a)
print(b)

print(id(a))
print(id(b))

b[2][0] = 300
print(a)
print(b)
'''
'''
# 집합 데이터 관련 api
# list
[1, 2, 3] 
- 값만 저장
- 리스트 자체는 변경 가능(요소 추가 삭제 가능)
- 요소 자체 변경 가능

# set
{1, 2, 3}
- 많이 사용 안함
- 집합
- 중복 허용 안함
- 순서 없음
- 변경 가능
- 요소는 변경 불가

# tuple
(1, 2, 3) (1,) 
- (1) <- , 없이 값이 하나만 들어가면 튜플이 아니라 괄호로 인식해 먼저 계산됨
- 자체 변경 불가
- 요소도 변경 불가(우회해서 변경 가능)
- 함수의 리턴값이 여러 개 표현 가능
- 함수의 파라메터나 리턴값으로 값을 주고 받을 때 값 변경 원하지 않을 때 활용 
- 파이썬에서 많이 사용함

# dictionary
{'키':'값', '키':'값'}
- 자체 변경 가능
- 키는 중복 허용 안함
'''
