from flask import request, render_template, redirect, Blueprint
import MMS.model.member as m

m_service = m.Service()
# Blueprint : route 등록 객체
bp = Blueprint('member', __name__, url_prefix='/member')


@bp.route('/list')
def member_list():
    mlist = m_service.printAll()
    return render_template('member/list.html', mlist=mlist)


@bp.route('/add')
def member_add_get():
    return render_template('member/addForm.html')


@bp.route('/add', methods=['POST'])
def member_add_post():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    m_service.addMember(m.Member(id=id, pwd=pwd, name=name, email=email))
    return redirect('/member/list')


@bp.route('/get')
def member_get():
    id = request.args.get('id', 0, str)   # url?뒤에 붙여보낸 파라메터 읽는 함수(파람이름, 디폴트값, 타입)
    m = m_service.getMemberById(id)
    return render_template('member/detail.html', m=m)


@bp.route('/edit', methods=['POST'])
def member_edit():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    m_service.editMember(m.Member(id=id, pwd=pwd, name=name, email=email))
    return redirect('/member/list')


@bp.route('/del')
def member_del():
    id = request.args.get('id', 0, str)
    m_service.delMember(id)
    return redirect('/member/list')
