"""
파일 입출력
1. 파일 오픈
file = open('파일경로', '모드')
# mode
- text mode : t 생략가능
r 읽기 : 파일이 없으면 에러
w 쓰기 : 파일이 있으면 그 파일 오픈, 내용이 있으면 지우고 오픈(새로쓰기), 파일이 없으면 새로 생성해서 오픈
a 이어쓰기 : 파일이 있고 파일에 내용이 있어도 지우지 않고 이어씀

# binary mode
rb / wb / ab

r+ / w+ / a+ > 읽고 쓰기

f = open('a.txt', 'r')

2. read / write
# 읽기함수
file.read() : 파일 전체 읽어서 반환
file.read(크기) : 크기만큼 읽어서 반환
file.readline() : 한줄 읽어서 반환

# 쓰기함수
file.write(출력값)
file.writelines(리스트, 튜플...) : 리스트나 튜플에 있는 값들을 파일에 출력

3. 파일 닫기
file.close()

# 상대경로
../ 상위
./ 동일
files 하위
"""

# 전체 읽기
f = open('files/a.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()

# f = open('../d0824/param_type.py', 'r', encoding='utf-8')
# data = f.read()
# print(data)

# 파일 크기만큼 읽기
# f2 = open('files/a.txt', 'r', encoding='utf-8')
# while True:
#     data = f2.read(5)
#     print(data)
#     if data == '':  # 파일의 끝을 만나면
#         break
#
# f2.close()

# 파일 한줄씩 읽기
f3 = open('files/a.txt', 'r', encoding='utf-8')
while True:
    data = f3.readline()
    print(data)
    if data == '':  # 파일의 끝을 만나면
        break

f3.close()