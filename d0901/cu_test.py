import warehouse_db.cu as cu
import warehouse_db.factory as f

fac = f.Service()
cu = cu.Service()


while True:
    mm = input('1.주문 2.주문목록 3.주문취소 4.결제 5.종료')
    if mm == '1':
        print('=== 주문 ===')
        fac.printAll()
        p = None
        while p == None:
            num = int(input('주문할 상품 번호 입력:'))
            p = fac.getProductByNum(num)
        cu.addOrder(p)
    elif mm == '2':
        cu.orderList()
    elif mm == '3':
        cu.delOrder()
    elif mm == '4':
        cu.pay()
    elif mm == '5':
        break