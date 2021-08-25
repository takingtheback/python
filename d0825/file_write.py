# f1 = open('files/b.txt', 'w', encoding='utf-8')
# while True:
#     data = input('메세지 입력. 멈추려면 /stop 입력 > ')
#     if data == '/stop':
#         break
#     f1.write(data + '\n')
# f1.close()

"""
파일 복사하는 함수를 만드시오.
파라메터: 원본파일명, 타깃파일명

파일 읽기 함수(파일명)
"""
# f3 = open('files/c.txt', 'w', encoding='utf-8')
# f = open('files/b.txt', 'r', encoding='utf-8')
# data = f.read()
# f3.write(data + '\n')
# f3.close()
#
# f2 = open('files/c.txt', 'r', encoding='utf-8')
# data = f2.read()
# print(data)
# f2.close()


def file_write(fname):
    f1 = open(fname, 'w', encoding='utf-8')
    while True:
        data = input('메세지 입력. 멈추려면 /stop 입력')
        if data == '/stop':
            break
        f1.write(data + '\n')
    f1.close()


def file_read(fname):
    f = open(fname, 'r', encoding='utf-8')
    msg = f.read()
    f.close()
    return msg


def file_write2(fname, msg):
    f = open(fname, 'w', encoding='utf-8')
    f.write(msg)
    f.close()


def file_copy(fname1, fname2):
    msg = file_read(fname1)
    file_write2(fname2, msg)
    print('복사 완료')


if __name__ == '__main__':
    file_copy('files/a.txt', 'files/c.txt')
    msg = file_read('files/c.txt')
    print('복사된 내용:')
    print(msg)
