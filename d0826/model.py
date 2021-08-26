class Member:
    def __init__(self, id='', pwd='', name='', email=''):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def printMem(self):
        print('id:', self.id)
        print('pwd:', self.pwd)
        print('name:', self.name)
        print('email:', self.email)


class MemDao:  # 저장소 작업 전담
    def __init__(self):
        self.members = []  # 저장소

    def insert(self, m):
        self.members.append(m)  # 멤버 객체 하나를 리스트에 추가

    def select(self, id):  # 리스트의 객체들을 하나씩 id 비교하여 같은 객체 반환
        for m in self.members:
            if m.id == id:
                return m

    def selectAll(self):
        return self.members

    def update(self, m):
        old = self.select(m.id)
        if old == None:
            return False
        else:
            old.pwd = m.pwd
            return True

    def delete(self, id):
        old = self.select(id)
        if old == None:
            return False
        else:
            self.members.remove(old)
            return True


class MemService:  # 비즈니스 로직
    def __init__(self):
        self.dao = MemDao()

    def addMember(self):
        m = 'asdf'
        while m != None:  # id 중복체크
            id = input('id:')
            m = self.dao.select(id)
        pwd = input('pwd:')
        name = input('name:')
        email = input('email:')
        m = Member(id, pwd, name, email)
        self.dao.insert(m)

    def getMember(self):
        id = input('search id:')
        m = self.dao.select(id)
        if m == None:
            print('없는 아이디')
        else:
            m.printMem()

    def printAll(self):
        mems = self.dao.selectAll()
        for m in mems:
            m.printMem()

    def editMember(self):
        id = input('수정할 id:')
        pwd = input('new pwd:')
        flag = self.dao.update(Member(id=id, pwd=pwd))
        if flag:
            print('수정완료')
        else:
            print('없는 아이디. 수정 취소됨')

    def delMember(self):
        id = input('삭제할 id:')
        flag = self.dao.delete(id)
        if flag:
            print('삭제완료')
        else:
            print('없는 아이디. 삭제 취소됨')


def run():
    service = MemService()
    while True:
        mm = input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료')
        if mm == '1':
            service.addMember()
        elif mm == '2':
            service.getMember()
        elif mm == '3':
            service.editMember()
        elif mm == '4':
            service.delMember()
        elif mm == '5':
            service.printAll()
        elif mm == '6':
            break


if __name__ == '__main__':
    run()
