'''
# OOP?
- 객체 지향 프로그래밍
어떻게 설명할지 스크립트 준비할 것

# 과제시 순서
- 기능 정리
- 주소(이름, 전화, 주소)
    -> {'name':'aaa', 'tel':1234, 'addr':'adf'}
1. 주소 추가
2. 주소 검색
3. 주소 수정
4. 주소 삭제
5. 주소 출력
'''

# 주소들 저장할 리스트
members = []

# 딕셔너리에서 사용할 키값
keys = ['name', 'tel', 'addr']

# 주소 추가
def addAddr():
    mem = {}
    for i in keys:
        mem[i] = input(i + ':')
        # 이름 중복 체크
        while i == 'name':
            d = getMember(mem[i])
            if d == None:   # 검색된 것이 없다. 중복안됨
                break
            else:
                print('중복된 이름, 다시 입력하시오')
                mem[i] = input(i + ':')

    members.append(mem)

# 주소 출력
def printMem(mem):
    for i in mem:
        print(i, ':', mem[i])

    print('================')

# 전체 출력
def printAll():
    for m in members:
        printMem(m)

# 검색 : 가입, 수정, 삭제 등에 이용될 초기 검색
# 파이썬은 리턴값이 없으면 None이 반환됨
def getMember(name):
    for m in members:
        if name == m['name']:
            return m

# 멤버 검색
def searchMember():
    name = input('검색할 사람의 이름: ')
    mem = getMember(name)
    if mem == None:
        print('없는 사람')
    else:
        printMem(mem)

# 멤버 수정
def editMember():
    name = input('수정할 사람의 이름: ')
    mem = getMember(name)
    if mem == None:
        print('없는 사람')
    else:
        for i in range(1, 3):
            mem[keys[i]] = input('new ' + keys[i] + ':')

# 멤버 삭제
def delMember():
    name = input('삭제할 사람의 이름: ')
    mem = getMember(name)
    if mem == None:
        print('없는 사람')
    else:
        members.remove(mem)

# 메뉴
def menu():
    while True:
        mm = input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료 > ')
        if mm =='1':
            addAddr()
        elif mm == '2':
            searchMember()
        elif mm == '3':
            editMember()
        elif mm == '4':
            delMember()
        elif mm == '5':
            printAll()
        elif mm == '6':
            break

# 메인
if __name__ == '__main__':
    menu()