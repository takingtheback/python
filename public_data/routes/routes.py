from flask import Flask, request, render_template, redirect, Blueprint
import models as mo
import matplotlib.pyplot as plt

bp = Blueprint('bus', __name__, url_prefix='/bus')

service = mo.BusService()


@bp.route('/route-info', methods=['POST'])
def route_info():
    routeid = request.form['routeid']
    bus: mo.Bus = service.getRouteInfo(routeId=routeid)
    return render_template('bus/businfo.html', bus=bus)


@bp.route('/route-path', methods=['POST'])
def route_path():
    routeid = request.form['routeid']
    stList:list = service.getStListByRouteId(routeId=routeid)
    return render_template('bus/stList.html', stList=stList, routeid=routeid)


@bp.route('/route-stationList', methods=['POST'])
def route_stationList():
    arsId = request.form['arsId']
    stList:list= service.getRouteByStationList(arsId=arsId)
    return render_template('bus/routeList.html', stList=stList, arsId=arsId)


@bp.route('/route-pathList', methods=['POST'])
def route_pathList():
    busRouteId = request.form['busRouteId']
    stList:list = service.getRoutePathList(busRouteId=busRouteId)
    return render_template('bus/pathList.html', stList=stList, busRouteId=busRouteId)


@bp.route('/IDList')
def IDList():
    stList:list = service.IDList()
    return render_template('bus/IDList.html', stList=stList)


@bp.route('/lineNameList')
def lineNameList():
    stList:list = service.lineNameList()
    return render_template('bus/lineNameList.html', stList=stList)


@bp.route('/stationIDList')
def stationIDList():
    stList:list = service.stationIDList()
    return render_template('bus/stationIDList.html', stList=stList)


@bp.route('/stationNameList')
def stationNameList():
    stList:list = service.stationNameList()
    return render_template('bus/stationNameList.html', stList=stList)

@bp.route('/graph', methods=['POST','GET']) # 없으면 get, 둘다 사용하려면 둘다 표기
def graph():
    img_path = '../static/graph/my_plot.png'

    x = [1, 2, 3, 4]
    y = [3, 8, 5, 6]
    fig, ax = plt.subplots()#그래프 이미지 객체 생성
    plt.plot(x, y) #fig 객체에 그래프를 그림
    fig.savefig(img_path)#fig 객체를 파라메터로 지정한 패스의 파일로 저장
    img_path = '/' + img_path
    return render_template('graph.html', img_path=img_path)


@bp.route('/route-time', methods=['POST'])
def route_time():
    arsId = request.form['arsId']
    busRouteId = request.form['busRouteId']
    times:list = service.getBustimeByStationList(arsId=arsId, busRouteId=busRouteId)
    return render_template('bus/five.html', times=times, arsId=arsId, busRouteId=busRouteId)

