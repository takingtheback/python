import warehouse_db.factory as f
fac = f.Service()

while True:
    mm = input('1.제품등록 2.번호검색 3.이름검색 4.수정 5.삭제 6.전체출력 7.상위메뉴 > ')
    if mm == '1':
        fac.addProduct()
    elif mm == '2':
        fac.getProductByNum()
    elif mm == '3':
        fac.getProductByName()
    elif mm == '4':
        fac.editProduct()
    elif mm == '5':
        fac.delProduct()
    elif mm == '6':
        fac.printAll()
    elif mm == '7':
        break