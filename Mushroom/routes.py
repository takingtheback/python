from flask import request, render_template, Blueprint
from models import mushroom_model

mush_bp = Blueprint('mushroom', __name__, url_prefix='/mushroom')
mush_service = mushroom_model.Service()


@mush_bp.route('/test')
def test():
    return render_template('test.html')


@mush_bp.route('/result1', methods=['POST'])
def result1():
    st = request.form['st']
    sw = request.form['sw']
    numOfRows = request.form['numOfRows']
    pageNo = request.form['pageNo']
    # print(st)
    # print(sw)
    # print(numOfRows)
    # print(pageNo)
    List = mush_service.Test(st=st, sw=sw, numOfRows=numOfRows, pageNo=pageNo)
    return render_template('result1.html', List=List)


@mush_bp.route('/result2', methods=['POST'])
def result2():
    st = request.form['st']
    sw = request.form['sw']
    numOfRows = request.form['numOfRows']
    pageNo = request.form['pageNo']
    # print(st)
    # print(sw)
    # print(numOfRows)
    # print(pageNo)
    List = mush_service.Test2(st=st, sw=sw, numOfRows=numOfRows, pageNo=pageNo)
    return render_template('result2.html', List=List)