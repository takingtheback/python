import os
dir = ''
def mkMemoDir():
    if not os.path.isdir(dir):
        os.mkdir(dir)

def selectFile():
    flist = os.listdir(dir)
    for idx, f in enumerate(flist):
        print(idx,'.',f)
    num = int(input('원하는 파일의 번호를 입력하시오'))
    return flist[num]

def readFile(fname):
    with open(dir+fname, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

def inputFileName():
    fname = input('작성할 파일명 입력:')
    path = dir+fname
    mode = 'w'
    while os.path.isfile(path):
        print('이미 존재하는 파일명. 다음 중 하나 선택')
        sel = int(input('1.새이름 입력 2.기존파일에 덮어쓰기 3.기존파일에 이어쓰기'))
        if sel==1:
            fname = input('작성할 파일명 입력:')
            path = dir + fname
        elif sel==2:
            break
        elif sel==3:
            mode = 'a'
            break
    return path, mode

def fileWrite(path, mode):
    with open(path, mode, encoding='utf-8') as f:
        while True:
            msg = input('msg(중단/stop):')
            if msg=='/stop':
                break
            f.write(msg+'\n')

if __name__ == '__main__':
    dir = 'memo/'
    mkMemoDir()
    while True:
        menu = input('1.읽기 2.쓰기 3.종료')
        if menu=='1':
            f = selectFile()
            readFile(f)
        elif menu=='2':
            path, mode = inputFileName()
            fileWrite(path, mode)
        elif menu=='3':
            break