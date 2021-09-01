import warehouse_db.factory as facto
import warehouse_db.cu as cu

class Menu:
    def __init__(self):
        self.__fac = facto.Service()
        self.__cu = cu.Service()

    def fac_run(self):#공장 메뉴
        while True:
            mm = input('1.제품등록 2.번호로검색 3.이름으로검색 4.수정 5.삭제 6.전체출력 7.상위메뉴')
            if mm=='1':
                self.__fac.addProduct()
            elif mm=='2':
                self.__fac.getProductByNum()
            elif mm=='3':
                self.__fac.getProductByName()
            elif mm=='4':
                self.__fac.editProduct()
            elif mm=='5':
                self.__fac.delProduct()
            elif mm=='6':
                self.__fac.printAll()
            elif mm=='7':
                break

    def cu_run(self):#편의점 메뉴
        while True:
            mm = input('1.주문 2.주문목록 3.주문취소 4.결제 5.상위메뉴')
            if mm=='1':
                print('=== 주문 ===')
                self.__fac.printAll()
                p = None
                while p==None:
                    num = int(input('주문할 상품 번호 입력:'))
                    p = self.__fac.getProductByNum(num)
                self.__cu.addOrder(p)
            elif mm=='2':
                self.__cu.orderList()
            elif mm=='3':
                self.__cu.delOrder()
            elif mm=='4':
                self.__cu.pay()
            elif mm=='5':
                break

    def run(self):#전체메뉴
        while True:
            mm = input('1.공장 2.편의점 3.종료')
            if mm=='1':
                self.fac_run()
            elif mm=='2':
                self.cu_run()
            elif mm=='3':
                break