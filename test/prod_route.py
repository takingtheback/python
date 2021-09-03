from flask import request, render_template, redirect, Blueprint
import models.factory as f

p_service = f.Service()
#Blueprint: route 등록 객체

bp = Blueprint('product', __name__, url_prefix='/product')

#route파일은 클라이언트 요청 url을 설계하고, 각 요청 url마다 실행할 코드를 함수로 등록
#웹에서는 요청을 url로 함

@bp.route('/list', methods=['POST', 'GET'])  #사용자가 기능 요청
def prod_list():
    arr = p_service.getAll()
    return render_template('product/list.html', plist=arr)  # plist:뷰페이지에서 부를 이름 / arr:전달할 값

@bp.route('/add')#get
def prod_add_get():
    return render_template('product/addForm.html')


@bp.route('/add', methods=['POST'])#post
def prod_add_post():
    name = request.form['name']  # request.form['폼양식이름']
    price = int(request.form['price'])
    amount = int(request.form['amount'])
    p_service.addProduct(f.Product(name=name, price=price, amount=amount))
    return redirect('/product/list')

@bp.route('/get')#제품 번호로 검색  '/product/get?num=3'
def prod_get():
    num = request.args.get('num', 0, int)#url?뒤에 붙여보낸 파라메터 읽는 함수(파람이름, 디폴트값, 타입)
    p = p_service.getProductByNum(num)
    return render_template('product/detail.html', p=p)


@bp.route('/edit', methods=['POST'])
def prod_edit():
    num = int(request.form['num'])
    name = request.form['name']  # request.form['폼양식이름']
    price = int(request.form['price'])
    amount = int(request.form['amount'])
    p_service.editProduct(f.Product(num=num, name=name, price=price, amount=amount))
    return redirect('/product/list')


@bp.route('/del')
def prod_del():
    num = request.args.get('num', 0, int)
    p_service.delProduct(num)
    return redirect('/product/list')

@bp.route('/prod-detail/<int:p_num>') #'/product/prod-detail/3'
def prod_order_detail(p_num):
    p = p_service.getProductByNum(p_num)
    return render_template('order/detail.html', p=p)
