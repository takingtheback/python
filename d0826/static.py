# 클래스 변수.
#객체 생성 유무와 상관없이 자동으로 하나 만들어서 이 클래스로 만든 모든 객체들이 공유
#사용: 클래스.변수
class StaticTest:
    a = 1   #클래스 변수.
    def __init__(self):
        self.b = 1  #객체 변수

    def add(self):
        StaticTest.a += 1
        self.b += 1

print('a:', StaticTest.a)

s1 = StaticTest()
s1.add()
print('a:', StaticTest.a, '/ b:', s1.b)

s2 = StaticTest()
s2.add()
print('a:', StaticTest.a, '/ b:', s2.b)

s3 = StaticTest()
s3.add()
print('a:', StaticTest.a, '/ b:', s3.b)

#클래스 메서드.
#클래스 소속이므로 객체 생성 없이 클래스 이름으로 호출
#클래스이름.메서드()

class StaticMethod:
    a = 1#클래스 변수
    def __init__(self):
        self.b = 1#객체 변수

    def method1(self):
        print('객체 멤버 메서드')
        print('a:', StaticMethod.a)
        print('b:', self.b)

    def method2():#클래스 메서드에서는 객체 멤버 변수 사용 불가
        print('클래스 메서드')
        print('a:', StaticMethod.a)
        #print('b:', self.b)  #에러

    def method3(self):
        self.method1()
        StaticMethod.method2()

    def method4():#클래스 메서드에서는 객체 메서드 호출 불가
        #self.method1()  #에러
        StaticMethod.method2()

s5 = StaticMethod()
s5.method1()
StaticMethod.method2()
s5.method3()
StaticMethod.method4()