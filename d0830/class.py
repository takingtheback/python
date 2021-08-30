"""
xml : 티스크립터 파일, 공공데이터
클래스
- vo(객체의 정보를 묶어줌)
- dao(database access object: DB 작업전담)
- service 비지니스로직

상속의 활용 목적

"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('좌표:(', self.x, ',', self.y, ')')


if __name__ == '__main__':

    points = []
    points.append(Point(1, 2))
    points.append(Point(3, 4))
    points.append(Point(5, 6))
    points.append(Point(7, 8))

    for p in points:
        p.printPoint()


class Test:  # 다양한 타입의 멤버변수
    def __init__(self):
        self.num = 0
        self.s = ''
        self.arr = []
        self.point = Point()  # 객체.포함관계 : 클래스타입의 멤버변수 / 관계(포함관계-has a , 상속관계 -is a)

    def printData(self):
        print('num:', self.num)
        print('s:', self.s)
        print('arr:', self.arr)
        self.point.x = 20
        self.point.y = 30
        self.point.printPoint()


def main():
    t1 = Test()  # 객체 생성
    t1.num = 10
    t1.s = 'hello class'
    t1.arr.append(1)
    t1.arr.append(2)
    t1.arr.append(3)
