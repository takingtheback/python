class Car:
    def horn(self):
        print('빵빵')


class Ambulance(Car):
    def horn(self):
        print('삐뽀삐뽀')


class FireEngine(Car):
    def horn(self):
        print('애애앵~')


class Bulldozer(Car):
    def horn(self):
        print('불~도저~')


if __name__ == '__main__':

    while True:
        obj = None
        sel = input('1.엠뷸런스 2.소방차 3.불도저 4.종료 > ')
        if sel == '1':
            obj = Ambulance()
        elif sel == '2':
            obj = FireEngine()
        elif sel == '3':
            obj = Bulldozer()
        elif sel == '4':
            break

        if obj is not None:
            obj.horn()
