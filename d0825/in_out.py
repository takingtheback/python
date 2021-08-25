"""
입출력
입력 : 데이터가 외부에서 프로그램 방향으로 흘러옴
출력 : 데이터가 프로그램에서 외부로 흘러나감

1. 표준입출력(stdio)
기본 제공 입출력
sys.stdin : 표준입력(키보드 입력)
sys.stdout : 표준출력(콘솔출력)
sys.stderr : 표준에러(콘솔에러출력)
"""


import sys
sysin = sys.stdin       # 표준입력 : read(바이트)
sysout = sys.stdout     # 표준출력 : write(출력내용) >> 반환값은 정상 출력 문자 수


num = sysout.write('글자를 입력하시오\n')
sysout.write('출력한 글자 수:' + str(num) + '\n')
data = sysin.read(5)
sysout.write('5개만 읽음' + data + '\n')
x = sysin.readline()
sysout.write('나머지 데이터' + x)
