#메서드 재정의: 상속받은 메서드를 고쳐서 사용.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('x:', self.x, ' / y:', self.y)

class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
    '''
    def printZ(self):
        print('z:', self.z)
    '''
    def printPoint(self):
        #print('x:', self.x, ' / y:', self.y, ' / z:', self.z)
        super().printPoint()
        print('z:', self.z)




if __name__ == '__main__':
    p1 = Point(2, 3)
    p1.printPoint()
    '''
    p2 = Point3D(4,5,6)
    p2.printPoint()
    p2.printZ()
    '''
    p3 = Point3D(6,7,8)
    p3.printPoint()