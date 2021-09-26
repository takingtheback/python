import requests
from bs4 import BeautifulSoup


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


# 서비스 : 기능구현, 멤버변수, 메서드
class BusService:

    #  이 클래스의 메서드들이 공통으로 사용하는 값
    def __init__(self):
        self.base_url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/'
        self.station_url = 'http://ws.bus.go.kr/api/rest/stationinfo/'
        self.api_key = 'z87XiFqBjizhP7gRBLRttGzJYgKrESmLrKQNmb1aVULKjUTS9f6TBr2rppZBMSEXbq1ovC5bUdGj2N%2FYD6pKPg%3D%3D'

    # route_id 를 받아서 정보 검색을 open-api에 요청
    # 요청에 대한 응답으로 xml 받음
    # 받은 xml 파싱=> 노선 정보 추출 => vo 에 담아서 반환

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
                routeType = '공항'
            elif routeType == '2':
                routeType = '마을'
            elif routeType == '3':
                routeType = '간선'
            elif routeType == '4':
                routeType = '지선'
            elif routeType == '5':
                routeType = '순환'
            elif routeType == '6':
                routeType = '광역'
            elif routeType == '7':
                routeType = '인천'
            elif routeType == '8':
                routeType = '경기'
            elif routeType == '9':
                routeType = '폐지'
            elif routeType == '0':
                routeType = '공용'
            else:
                routeType = '기타'
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
            print('오류발생 code:', code)

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
            print('오류발생 code:', code)

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
                    busRouteType = '공항'
                elif busRouteType == '2':
                    busRouteType = '마을'
                elif busRouteType == '3':
                    busRouteType = '간선'
                elif busRouteType == '4':
                    busRouteType = '지선'
                elif busRouteType == '5':
                    busRouteType = '순환'
                elif busRouteType == '6':
                    busRouteType = '광역'
                elif busRouteType == '7':
                    busRouteType = '인천'
                elif busRouteType == '8':
                    busRouteType = '경기'
                elif busRouteType == '9':
                    busRouteType = '폐지'
                elif busRouteType == '0':
                    busRouteType = '공용'
                else:
                    busRouteType = '기타'
                stBegin = item.find('stBegin').get_text()
                stEnd = item.find('stEnd').get_text()
                term = item.find('term').get_text()
                nextBus = item.find('nextBus').get_text()
                # firstBusTm = item.find('firstBusTm').get_text()
                tm = item.find('firstBusTm').get_text()
                hour = tm[8:10]
                min = tm[10:12]
                firstBusTm = hour + ':' + min

                # lastBusTm = item.find('lastBusTm').get_text()
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
            print('오류발생 code:', code)

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
            print('오류발생 code:', code)

        return stations