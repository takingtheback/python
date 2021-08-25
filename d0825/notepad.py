import os


def makeFolder():
    if os.path.isdir('memo') == False:
        os.mkdir('memo')
    else:
        None


def list():
    dir_name = os.getcwd()
    os.chdir('memo')
    files = os.listdir('./')
    print(dir_name, '디렉토리의 파일 목록')
    for i in enumerate(files):
        print(i)

    fno = input('확인할 파일명 > ')
    f = open(fno, 'r', encoding='utf-8')
    data = f.read()
    print(data)
    os.chdir('../')
    f.close()



def write():
    fname = input('파일명 입력 > ')
    os.chdir('memo')
    f1 = open(fname, 'w', encoding='utf-8')
    while True:
        data = input('메세지 입력. 멈추려면 /stop 입력')
        if data == '/stop':
            break
        f1.write(data + '\n')

    os.chdir('../')
    f1.close()


def menu():
    while True:
        no = input('1.읽기 2.쓰기 3.종료  > ')
        if no == '1':
            list()
        elif no == '2':
            write()
        elif no == '3':
            break


if __name__ == '__main__':
    makeFolder()
    menu()
