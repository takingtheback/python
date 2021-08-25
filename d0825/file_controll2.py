"""
<파일제어>
1)파일절삭
지정한 크기로 파일 단편화
file.truncate(size)

f = open('files/d.txt', 'wb+')
f.truncate(5)
f.close

2)파일명 바꾸기
os.rename(old, new)

import os
os.rename('files/d.txt', 'files/d2.txt')

3) 파일 삭제
os.remove(파일명)

4)현재 작업디렉토리
os.getcwd()

5)작업 디렉토리 변경
os.chdir(path)

6)디렉토리 생성
os.mkdir(path)

7)디렉토리 삭제
os.rmdir(path)

8)디렉토리 안에 있는 파일 목록
os.listdir(path)

9)파일 존재 확인
os.path.isfile(path) => 파일 있으면 True, 없으면 False

10)디렉토리 존재 확인
os.path.isdir(path) => 디렉토리 있으면 True, 없으면 False
'''
"""

import os

dir_name = os.getcwd()
print('현재 작업 디렉토리:', dir_name)
print('files로 디렉토리 이동')
os.chdir('files')
dir_name = os.getcwd()
print('현재 작업 디렉토리:', dir_name)
files = os.listdir('./')
print(dir_name, '디렉토리의 파일 목록')
for f in files:
    print(f)

del_file = input('삭제할 파일명 입력')
os.remove(del_file)

files = os.listdir('./')
print(dir_name, '디렉토리의 파일 목록')
for f in files:
    print(f)

os.mkdir('test') #test 디렉토리 생성
ff = open('test/a.txt', 'w')
ff.write('hello')
ff.close()

files = os.listdir('./test')
print(dir_name, '/test 디렉토리의 파일 목록')
for f in files:
    print(f)