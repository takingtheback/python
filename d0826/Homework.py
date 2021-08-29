"""
공장과 편의점
1. 공장
- 하위메뉴
    1.제품등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료(상위메뉴)
2. 편의점
- 하위메뉴
    1.주문 2.주문취소 3.주문목록 4.결제 5.종료(상위메뉴)
3. 종료(프로그램 종료)

# 공장
- 제품등록
    - 제품번호(자동할당, 시퀀스)
    - 제품명
    - 가격
    - 수량

# 편의점
- 주문
    - 주문번호(자동할당)
    - 주문상품(product) : 공장에서 등록된 제품
    - 주문수량
    - 결제금액(단가 * 주문수량)
    - 결제유무(True/False)

- 주문취소
    - 결제된 제품은 취소 안됨

- 결제
    - 결제대상(결제유무가 False) 보여주고 사용자가 선택
"""
import sys


class order:
    def __init__(self, oNo='', oProduct='', oQuantity='', oPrice='', paid='False'):
        self.oNo = oNo
        self.oProduct = oProduct
        self.oQuantity = oQuantity
        self.oPrice = oPrice
        self.paid = paid

    def printOrder(self):
        print('주문번호:', self.oNo)
        print('주문상품:', self.oProduct)
        print('주문수량:', self.oQuantity)
        print('금액:', self.oPrice)
        print('paid:', self.paid)
        print('___________________')


class oDao:  # 저장소 작업 전담
    def __init__(self):
        self.orders = []  # 저장소

    def insert(self, o):
        self.orders.append(o)  # 멤버 객체 하나를 리스트에 추가

    def select(self, oNo):  # 리스트의 객체들을 하나씩 id 비교하여 같은 객체 반환
        for o in self.orders:
            if o.oNo == oNo:
                return o

    def selectAll(self):
        return self.orders

    def update(self, o):
        old = self.select(o.oNo)
        if old == None:
            return False
        else:
            old.paid = o.paid
            return True

    def delete(self, oNo):
        old = self.select(oNo)
        if old == None:
            return False
        else:
            self.orders.remove(old)
            return True


class orderService:
    oNo = 0

    def __init__(self):
        self.dao = oDao()

    def addOrder(self):
        o = 0
        while o != None:  # id 중복체크
            orderService.oNo += 1
            oNo = int(orderService.oNo)
            o = self.dao.select(oNo)
        oProduct = input('oProduct:')
        oQuantity = input('oQuantity:')
        oPrice = input('oPrice:')
        paid = False
        o = order(oNo, oProduct, oQuantity, oPrice, paid)
        self.dao.insert(o)

    def getOrder(self):
        oNo = int(input('검색할 주문번호:'))
        o = self.dao.select(oNo)
        if o == None:
            print('없는 주문번호')
        else:
            o.printOrder()

    def printAll(self):
        orders = self.dao.selectAll()
        for o in orders:
            o.printOrder()

    def editOrder(self):
        oNo = int(input('결제할 주문번호:'))
        paid = 'true'
        flag = self.dao.update(order(oNo=oNo, paid=paid))
        if flag:
            print('결제 완료')
        else:
            print('없는 아이디. 결제 취소됨')

    def delOrder(self):
        oNo = int(input('취소할 주문번호:'))
        flag = self.dao.delete(oNo)

        if flag:
            print('취소 완료')
        else:
            print('없는 주문번호')


class product:
    No = 0

    def __init__(self, pNo='', pName='', pPrice='', pQuantity=''):
        self.pNo = pNo
        self.pName = pName
        self.pPrice = pPrice
        self.pQuantity = pQuantity

    def printProduct(self):
        print('pNo:', self.pNo)
        print('pName:', self.pName)
        print('pPrice:', self.pPrice)
        print('pQuantity:', self.pQuantity)
        print('___________________')

    def printProductList(self):
        product.No += 1
        pN = product.No
        print(pN, ':', self.pName)


class pDao:  # 저장소 작업 전담
    def __init__(self):
        self.products = []  # 저장소

    def insert(self, p):
        self.products.append(p)  # 멤버 객체 하나를 리스트에 추가

    def select(self, pNo):  # 리스트의 객체들을 하나씩 id 비교하여 같은 객체 반환
        for p in self.products:
            if p.pNo == pNo:
                return p

    def selectAll(self):
        return self.products

    def update(self, p):
        old = self.select(p.pNo)
        if old == None:
            return False
        else:
            old.pName = p.pName
            old.pPrice = p.pPrice
            old.pQuantity = p.pQuantity
            return True

    def delete(self, pNo):
        old = self.select(pNo)
        if old == None:
            return False
        else:
            self.products.remove(old)
            return True


class factoryService:
    pNo = 0

    def __init__(self):
        self.dao = pDao()

    def addProduct(self):
        p = 0
        while p != None:  # id 중복체크
            factoryService.pNo += 1
            pNo = int(factoryService.pNo)
            # pNo = input('pNo:')
            p = self.dao.select(pNo)

        pName = input('pName:')
        pPrice = input('pPrice:')
        pQuantity = input('pQuantity:')

        p = product(pNo, pName, pPrice, pQuantity)
        self.dao.insert(p)

    def getProduct(self):
        pNo = int(input('검색할 제품번호:'))
        p = self.dao.select(pNo)
        if p != None:
            p.printProduct()
        else:
            print('없는 제품번호')
        # if p == None:
        #     print('없는 제품번호')
        # else:
        #     p.printProduct()

    def printAll(self):
        products = self.dao.selectAll()
        for p in products:
            p.printProduct()

    def printProductList(self):
        products = self.dao.selectAll()
        for p in products:
            p.printProductList()

    def editProduct(self):
        pNo = int(input('수정할 제품번호:'))
        pName = input('수정할 제품명:')
        pPrice = input('수정할 가격:')
        pQuantity = input('수정할 수량:')
        flag = self.dao.update(product(pNo=pNo, pName=pName, pPrice=pPrice, pQuantity=pQuantity))
        if flag:
            print('수정완료')
        else:
            print('없는 아이디. 수정 취소됨')

    def delProduct(self):
        pNo = int(input('삭제할 제품번호:'))
        flag = self.dao.delete(pNo)
        if flag:
            print('삭제완료')
        else:
            print('없는 아이디. 삭제 취소됨')


def factory():
    service = factoryService()
    while True:
        no = input('1.제품등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료(상위메뉴) > ')
        if no == '1':
            service.addProduct()
        elif no == '2':
            service.getProduct()
        elif no == '3':
            service.editProduct()
        elif no == '4':
            service.delProduct()
        elif no == '5':
            # service.printAll()
            service.printProductList()
        elif no == '6':
            menu()


def convenience():
    service = orderService()
    while True:
        no = input('1.주문 2.주문취소 3.주문목록 4.결제 5.종료(상위메뉴) > ')
        if no == '1':
            service.addOrder()
        elif no == '2':
            service.delOrder()
        elif no == '3':
            service.printAll()
        elif no == '4':
            service.editOrder()
        elif no == '5':
            menu()


def menu():
    while True:
        no = input('1.공장 2.편의점 3.종료 > ')
        if no == '1':
            factory()
        elif no == '2':
            convenience()
        elif no == '3':
            sys.exit()


if __name__ == '__main__':
    menu()
