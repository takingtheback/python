import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import render_template


class Bus:
    def __init__(self, route_id=None, bus_name=None, st_station=None, ed_station=None, term=None, first_tm=None,
                 last_tm=None, corp_name=None, length=None, routeType=None):
        self.route_id = route_id
        self.bus_name = bus_name
        self.st_station = st_station
        self.ed_station = ed_station
        self.term = term
        self.first_tm = first_tm
        self.last_tm = last_tm
        self.corp_name = corp_name
        self.length = length
        self.routeType = routeType

    # to_String (Debug)
    # def __str__


class Station:
    def __init__(self, seq=None, arsId=None, stationNm=None, beginTm=None, lastTm=None, gpsX=None, gpsY=None):
        self.seq = seq
        self.arsId = arsId
        self.stationNm = stationNm
        self.beginTm = beginTm
        self.lastTm = lastTm
        self.gpsX = gpsX
        self.gpsY = gpsY


class Station2:
    def __init__(self, busRouteId=None, busRouteNm=None, length=None, busRouteType=None, stBegin=None, stEnd=None,
                 term=None, nextBus=None, firstBusTm=None, lastBusTm=None, firstBusTmLow=None, lastBusTmLow=None):
        self.busRouteId = busRouteId
        self.busRouteNm = busRouteNm
        self.length = length
        self.busRouteType = busRouteType
        self.stBegin = stBegin
        self.stEnd = stEnd
        self.term = term
        self.nextBus = nextBus
        self.firstBusTm = firstBusTm
        self.lastBusTm = lastBusTm
        self.firstBusTmLow = firstBusTmLow
        self.lastBusTmLow = lastBusTmLow


class RoutePath:
    def __init__(self, no=None, gpsX=None, gpsY=None, posX=None, posY=None):
        self.no = no
        self.gpsX = gpsX
        self.gpsY = gpsY
        self.posX = posX
        self.posY = posY


class IDList:
    def __init__(self, id=None):
        self.id = id

class Station5:
    def __init__(self, arsId=None, stationNm=None, busRouteId=None, busRouteNm=None, firstBusTm=None, lastBusTm=None):
        self.arsId=arsId
        self.stationNm=stationNm
        self.busRouteId=busRouteId
        self.busRouteNm=busRouteNm
        self.firstBusTm=firstBusTm
        self.lastBusTm=lastBusTm


# ????????? : ????????????, ????????????, ?????????
class BusService:

    #  ??? ???????????? ??????????????? ???????????? ???????????? ???
    def __init__(self):
        self.base_url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/'
        self.station_url = 'http://ws.bus.go.kr/api/rest/stationinfo/'
        self.api_key = 'z87XiFqBjizhP7gRBLRttGzJYgKrESmLrKQNmb1aVULKjUTS9f6TBr2rppZBMSEXbq1ovC5bUdGj2N%2FYD6pKPg%3D%3D'

    # route_id ??? ????????? ?????? ????????? open-api??? ??????
    # ????????? ?????? ???????????? xml ??????
    # ?????? xml ??????=> ?????? ?????? ?????? => vo ??? ????????? ??????

    def getRouteInfo(self, routeId: str):
        cmd = '/getRouteInfo'
        url = self.base_url + cmd + '?ServiceKey=' + self.api_key + '&busRouteId=' + routeId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').text
        if code == '0':
            bus_id = root.find('busRouteId').get_text()
            bus_name = root.find('busRouteNm').get_text()
            length = root.find('length').get_text()
            routeType = root.find('routeType').get_text()
            if routeType == '1':
                routeType = '??????'
            elif routeType == '2':
                routeType = '??????'
            elif routeType == '3':
                routeType = '??????'
            elif routeType == '4':
                routeType = '??????'
            elif routeType == '5':
                routeType = '??????'
            elif routeType == '6':
                routeType = '??????'
            elif routeType == '7':
                routeType = '??????'
            elif routeType == '8':
                routeType = '??????'
            elif routeType == '9':
                routeType = '??????'
            elif routeType == '0':
                routeType = '??????'
            else:
                routeType = '??????'
            edstation = root.find('edStationNm').get_text()
            ststation = root.find('stStationNm').get_text()
            # firsttm = root.find('firstBusTm').get_text()
            tm = root.find('firstBusTm').get_text()
            hour = tm[8:10]
            min = tm[10:12]
            firsttm = hour + ':' + min

            # lasttm = root.find('lastBusTm').get_text()
            tm = root.find('lastBusTm').get_text()
            hour = tm[8:10]
            min = tm[10:12]
            lasttm = hour + ':' + min

            term = root.find('term').get_text()
            corp_name = root.find('corpNm').get_text()

            return Bus(route_id=bus_id, bus_name=bus_name, st_station=ststation, ed_station=edstation, term=term,
                       first_tm=firsttm, length=length, routeType=routeType, last_tm=lasttm, corp_name=corp_name)

        else:
            print('???????????? code:', code)

    def getStListByRouteId(self, routeId: str):
        cmd = '/getStaionByRoute'
        url = self.base_url + cmd + '?ServiceKey=' + self.api_key + '&busRouteId=' + routeId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').text
        stations = []
        if code == '0':
            # items = root.select('itemList')
            items = root.find_all('itemList')
            for item in items:
                seq = item.find('seq').get_text()
                arsId = item.find('arsId').get_text()
                stationNm = item.find('stationNm').get_text()
                beginTm = item.find('beginTm').get_text()
                lastTm = item.find('lastTm').get_text()
                gpsX = item.find('gpsX').get_text()
                gpsY = item.find('gpsY').get_text()
                stations.append(Station(seq=seq, arsId=arsId, stationNm=stationNm, beginTm=beginTm, lastTm=lastTm, gpsX=gpsX, gpsY=gpsY))
        else:
            print('???????????? code:', code)

        return stations

    def getRouteByStationList(self, arsId: str):
        cmd = '/getRouteByStation'
        url = self.station_url + cmd + '?ServiceKey=' + self.api_key + '&arsId=' + arsId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').text
        station = []
        if code == '0':
            # items = root.select('itemList')
            items = root.find_all('itemList')
            for item in items:
                busRouteId = item.find('busRouteId').get_text()
                busRouteNm = item.find('busRouteNm').get_text()
                length = item.find('length').get_text()
                busRouteType = item.find('busRouteType').get_text()
                if busRouteType == '1':
                    busRouteType = '??????'
                elif busRouteType == '2':
                    busRouteType = '??????'
                elif busRouteType == '3':
                    busRouteType = '??????'
                elif busRouteType == '4':
                    busRouteType = '??????'
                elif busRouteType == '5':
                    busRouteType = '??????'
                elif busRouteType == '6':
                    busRouteType = '??????'
                elif busRouteType == '7':
                    busRouteType = '??????'
                elif busRouteType == '8':
                    busRouteType = '??????'
                elif busRouteType == '9':
                    busRouteType = '??????'
                elif busRouteType == '0':
                    busRouteType = '??????'
                else:
                    busRouteType = '??????'
                stBegin = item.find('stBegin').get_text()
                stEnd = item.find('stEnd').get_text()
                term = item.find('term').get_text()
                nextBus = item.find('nextBus').get_text()
                # firstBusTm = item.find('firstBusTm').get_text()
                tm = item.find('firstBusTm').get_text()
                hour = tm[8:10]
                min = tm[10:12]
                firstBusTm = hour + ':' + min

                # lastBusTm = item.find('lastBusTm').get_text() 2109280945300000
                tm = item.find('lastBusTm').get_text()
                hour = tm[8:10]
                min = tm[10:12]
                lastBusTm = hour + ':' + min

                # firstBusTmLow = item.find('firstBusTmLow').get_text()
                tm = item.find('firstBusTmLow').get_text()
                hour = tm[8:10]
                min = tm[10:12]
                firstBusTmLow = hour + ':' + min

                # lastBusTmLow = item.find('lastBusTmLow').get_text()
                tm = item.find('lastBusTmLow').get_text()
                hour = tm[8:10]
                min = tm[10:12]
                lastBusTmLow = hour + ':' + min

                station.append(
                    Station2(busRouteId=busRouteId, busRouteNm=busRouteNm, length=length, busRouteType=busRouteType,
                             stBegin=stBegin, stEnd=stEnd, term=term, nextBus=nextBus, firstBusTm=firstBusTm,
                             lastBusTm=lastBusTm, firstBusTmLow=firstBusTmLow, lastBusTmLow=lastBusTmLow))
        else:
            if code == '1':
                msg = '????????? ????????? ?????????????????????'
            elif code == '2':
                msg = '????????? ?????? ???????????????. ?????? ????????? ???????????? ???????????????.'
            elif code == '3':
                msg = '???????????? ?????? ??? ????????????'
            elif code == '4':
                msg = '????????? ?????? ??? ????????????.'
            elif code == '5':
                msg = '????????? ????????? ????????? ???????????????. ???/?????? ????????? ???????????? ???????????????'
            elif code == '6':
                msg = '????????? ????????? ?????? ??? ????????????. ?????? ??? ?????? ???????????????'
            elif code == '7':
                msg = '?????? ?????? ????????? ???????????? ????????????.'
            elif code == '8':
                msg = '?????? ?????????????????????.'
            else:
                msg = '??? ??? ?????? ???????????????.'
            print(msg)
        return station

    def getRoutePathList(self, busRouteId: str):
        cmd = '/getRoutePath'
        url = self.base_url + cmd + '?ServiceKey=' + self.api_key + '&busRouteId=' + busRouteId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').text
        stations = []
        if code == '0':
            # items = root.select('itemList')
            items = root.find_all('itemList')
            for item in items:
                no = item.find('no').get_text()
                gpsX = item.find('gpsX').get_text()
                gpsY = item.find('gpsY').get_text()
                posX = item.find('posX').get_text()
                posY = item.find('posY').get_text()
                stations.append(RoutePath(no=no, gpsX=gpsX, gpsY=gpsY, posX=posX, posY=posY))
        else:
            print('???????????? code:', code)

        return stations

    def IDList(self):
        df = pd.read_excel('bus_station_info.xlsx', engine='openpyxl')
        data = df[['??????ID']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
        id = data.values
        list = []
        for i in id:
            list.append(IDList(id=i))
        return list

    def lineNameList(self):
        df = pd.read_excel('bus_station_info.xlsx', engine='openpyxl')
        data = df[['?????????']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
        id = data.values
        list = []
        for i in id:
            list.append(IDList(id=i))
        return list

    def stationIDList(self):
        df = pd.read_excel('bus_station_info.xlsx', engine='openpyxl')
        data = df[['ARS-ID']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
        id = data.values
        list = []
        for i in id:
            list.append(IDList(id=i))
        return list

    def stationNameList(self):
        df = pd.read_excel('bus_station_info.xlsx', engine='openpyxl')
        data = df[['????????????']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
        id = data.values
        list = []
        for i in id:
            list.append(IDList(id=i))
        return list

    def getBustimeByStationList(self, arsId: str, busRouteId: str):  # 5
        cmd = '/getBustimeByStation'
        url = self.station_url + cmd + '?ServiceKey=' + self.api_key + '&arsId=' + arsId + '&busRouteId=' + busRouteId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').text
        times = []
        if code == '0':
            items = root.find_all('itemList')
            for item in items:
                arsId = item.find('arsId').text
                stationNm = item.find('stationNm').text
                busRouteId = item.find('busRouteId').text
                busRouteNm = item.find('busRouteNm').text
                firstBusTm = item.find('firstBusTm').text
                lastBusTm = item.find('lastBusTm').text
                times.append(Station5(arsId=arsId, stationNm=stationNm, busRouteId=busRouteId, busRouteNm=busRouteNm,
                                      firstBusTm=firstBusTm, lastBusTm=lastBusTm))
        else:
            print('???????????? code:', code)

        return times
