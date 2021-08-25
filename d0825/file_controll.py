"""
파일커서 위치 제어
tell() : 현재 커서 위치 반환
seek(off, whence) : 커서 위치 이동. whence(0: 맨앞, 1: 현재위치, 2:맨뒤)를 기준점으로 하여 off만큼 떨어진 위치로 이동
"""

f = open('files/d.txt', 'rb')
data = f.read(3)
print('data:', data)
print('tell():', f.tell())

print('현재 위치를 기준으로 5칸 뒤로 이동')
f.seek(5, 1)
print('tell():', f.tell())
data = f.read(1)
print('data:', data)
print('tell():', f.tell())

print('현재 위치를 기준으로 3칸 앞으로 이동')
f.seek(-3, 1)
print('tell():', f.tell())
data = f.read(1)
print('data:', data)
print('tell():', f.tell())

print('맨앞을 기준으로 5칸 뒤로 이동')
f.seek(5, 0)
print('tell():', f.tell())
data = f.read(1)
print('data:', data)
print('tell():', f.tell())

print('맨뒤를 기준으로 5칸 앞으로 이동')
f.seek(-5, 2)
print('tell():', f.tell())
data = f.read(1)
print('data:', data)
print('tell():', f.tell())

f.close()