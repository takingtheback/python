"""
java
class Test {
    int x;
    int y;
    public Test(int x, int y) {
        t1.x = x;
        t1.y = y;
    }
}

class Main {
    public static voic main(String[] args) {
    Test t1 = new Test();
    }
}
"""
class Product:
    cnt = 12
    def __init__(self,name): # 객체 메서드의 첫번째 파라메터는 파이썬 시스템이 현재 이 객체의 참조값을 자동으로 넣어줌
        self.num = 0
        self.name = name
        self.price = 0
        self.amount = 0


print(Product.cnt)
p1 = Product('aaa')
p2 = Product('bbb')

"""
캐스팅 함수, 형변환
str(): 정수나 실수, bool 타입의 값을 문자열로 변환
int(): 문자열 숫자나 실수를 정수로 변환
float(): 문자열 실수나 정수를 실수로 변환
"""
print(str(12))
print(type(str(12)))
print(str(3.14))
print(type(str(3.14)))
print(str(True))
print(type(str(True)))
print(int(3.14))
print(type(int(3.14)))


