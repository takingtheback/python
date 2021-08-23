'''
비어있는 주소록

1. 추가 2. 검색 3. 수정 4. 삭제 5.전체출력
addr=[]

추가함수
한 사람의 정보 입력받아 딕셔너리로 생성하여 리스트에 추가
(추가시 중복입력 방지)
{'name':'aaa', 'tel':'111','addr':'asdf'}

검색함수
검색할 이름 입력받음
addr 각 방의 name 키 값 비교 있나 없나 검색
있으면 출력, 없으면 'not found'

수정함수
수정할 사람의 이름과 새 전화번호, 새 주소를 입력받아서
수정할 사람 이름으로 검색한 후 있으면 새 딕셔너리로 교체.

삭제함수
삭제할 사람의 이름 입력받아 검색해서 있으면
그 칸 삭제

전체 출력 함수
addr 전체 내용 출력
'''

import sys
addr=[]

# 초기항목추가
def add_addr(name, tel, add):
    addr.append({'name': name, 'tel': tel, 'add': add})

add_addr('aaa', 1, 'seoul')
add_addr('bbb', 2, 'busan')
add_addr('ccc', 3, 'daegu')

while True:
    menu = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 > '))
    if menu == 1:
        print(' 추가하려는 사람의 이름, 번호, 주소를 입력하세요.')

        name = input('이름 : ')
        for i in range(0, len(addr)):
            if (addr[i]['name'] == name):
                print(' 추가하려는 사람의 이름이 중복됩니다. 다른 이름을 선택해주세요.')
                break
            else:
                tel = input('번호 : ')
                add = input('주소 : ')
                addr.append({'name':name, 'tel':tel,'add':add})
                break

    if menu == 2:
        print('검색하려는 사람의 이름을 입력하세요.')
        name = input('이름 : ')
        for i in range(0, len(addr)):
            if (addr[i]['name'] == name):
               print(addr[i])
               break
            else:
                print('not found')

    if menu == 3:
        print('검색하려는 사람의 이름을 입력하세요.')
        name = input('이름 : ')
        for i in range(0, len(addr)):
            if (addr[i]['name'] == name):
                print('변경사항을 입력하세요.')
                modifiedname = input('이름 : ')
                modifiedtel = input('번호 : ')
                modifiedadd = input('주소 : ')
                addr[i]['name'] = modifiedname
                addr[i]['tel'] = modifiedtel
                addr[i]['add'] = modifiedadd
                break
            else:
                print('not found')

    if menu == 4:
        print(' 삭제하려는 사람의 이름을 입력하세요.')
        name = input('이름 : ')
        for i in range(0, len(addr)):
            if (addr[i]['name'] == name):
                del(addr[i])
                print(i, '번 딕셔너리를 삭제했습니다.')
                break
            else:
                print('not found')
    if menu == 5:
        print('전체 출력')

        def print_addr():
            for i in addr:
                print(i, end=', ')
        print_addr()
        print()
