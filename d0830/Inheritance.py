class Parent:
    def __init__(self):
        self.a = 10

    def parent_method(self):
        print('parent_method')

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.b = 'child'

    def child_method(self):
        print('child_method')


class Child2(Parent):
    def __init__(self, name='', tel=''):
        super().__init__()
        self.name = name
        self.tel = tel

    def printInfo(self):
        print('a:', self.a)
        print('name:', self.name)
        print('tel:', self.tel)


if __name__ == '__main__':
    p1 = Parent()
    print(p1.a)
    p1.parent_method()

    c1 = Child()
    print(c1.a)
    print(c1.b)
    c1.parent_method()
    c1.child_method()

    c2 = Child2('aaaa', '1234')
    c2.parent_method()
    c2.printInfo()
    