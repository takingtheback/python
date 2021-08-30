'''
학사관리 프로그램

학생:수강과목[] / 수강과목추가()
교직원: 직무. / 직무 변경()
교수: 개설과목[] / 개설과목 추가()

person
이름
부서(학과)
번호
전화번호
-------------
정보출력 메서드
'''
class Subject:
    def __init__(self, num='', name=''):
        self.num = num
        self.name = name

    def print(self):
        print(str(self.num) + '.' + self.name)

class Person:
    def __init__(self, num='', name='', dept='', tel=''):
        self.num = num
        self.name = name
        self.dept = dept
        self.tel = tel

    def printInfo(self):
        print('num:', self.num)
        print('name:', self.name)
        print('dept:', self.dept)
        print('tel:', self.tel)

class Student(Person):#교수가 개설한 과목중 선택해서 수강
    def __init__(self, num='', name='', dept='', tel=''):
        super().__init__(num=num, name=name, dept=dept, tel=tel)
        self.subjects=[]  #수강 과목들

    def addSubject(self, sub):
        self.subjects.append(sub)

    def printSubjects(self):
        print('수강과목들')
        for s in self.subjects:
            s.print()

class Prof(Person): #교직원이 등록한 과목중 선택해서 개설
    def __init__(self, num='', name='', dept='', tel=''):
        super().__init__(num=num, name=name, dept=dept, tel=tel)
        self.open_subs = [] #개설 과목들

    def addOpensubj(self, sub):
        self.open_subs.append(sub)

    def printOpenSubs(self):
        print('개설과목들')
        for s in self.open_subs:
            s.print()

class Staff(Person):  #과목 등록
    def __init__(self, num='', name='', dept='', tel='', job=''):
        super().__init__(num=num, name=name, dept=dept, tel=tel)
        self.job = job

    def addSubject(self, sub_list):
        num = int(input('과목번호'))
        name = input('과목이름')
        sub_list.append(Subject(num, name))

    def printSubjects(self, sub_list):
        print('현재 학기 등록 과목')
        for s in sub_list:
            s.print()

class Service:
    def __init__(self):
        self.stu = Student(num='stu01', name='aaa', dept='멀티미디어학과', tel='1234')
        self.prof = Prof(num='prof05', name='bbb', dept='정보통신학과', tel='5678')
        self.staff = Staff(num='staff23', name='ccc', dept='hr', tel='468678')
        self.subs = []

    def addSubject(self):#교직원 과목 등록
        self.staff.addSubject(self.subs)

    def printAllSubjects(self):#등록된 모든 과목 출력
        self.staff.printSubjects(self.subs)

    def openSub(self):#교수 과목 개설
        print(self.prof.name+'교수의 과목 개설')
        self.printAllSubjects()
        num = int(input('개설할 과목 번호:'))
        for s in self.subs:
            if s.num == num:
                self.prof.addOpensubj(s)
                print(s.name + '개설 완료')

    def printOpenSub(self):
        self.prof.printOpenSubs()

    def addSugang(self):
        print('현재 개설된 과목')
        self.printOpenSub()
        num = int(input('수강할 과목 번호:'))
        for s in self.prof.open_subs:
            if s.num == num:
                self.stu.addSubject(s)
                print(s.name+'수강신청 완료')

    def printSugang(self):
        self.stu.printSubjects()


if __name__ == '__main__':
    service = Service()
    service.stu.printInfo()
    service.prof.printInfo()
    service.staff.printInfo()

    service.addSubject()
    service.addSubject()
    service.addSubject()
    service.addSubject()

    service.openSub()
    service.openSub()
    service.openSub()

    service.addSugang()
    service.addSugang()

    service.printSugang()