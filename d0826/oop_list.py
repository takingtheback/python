class Member:
    def __init__(self, id=None, pwd=None, name=None, email=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def printMem(self):
        print('id:', self.id)
        print('pwd:', self.pwd)
        print('name:', self.name)
        print('email:', self.email)

def inputMem():     # 전역 함수
    id = input('id:')
    pwd = input('pwd:')
    name = input('name:')
    email = input('email:')
    # m = Member(id, pwd, name, email)
    # return m
    return Member(id, pwd, name, email)

if __name__ == '__main__':
    members=[]
    for i in range(0,3):
        members.append(inputMem())

    for m in members:
        m.printMem()
    

   # m1 = inputMem()
   # m2 = inputMem()
   # m3 = inputMem()
   #
   # m1.printMem()
   # m2.printMem()
   # m3.printMem()