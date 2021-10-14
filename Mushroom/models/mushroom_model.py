import requests
from bs4 import BeautifulSoup


class Mushroom:
    def __init__(self, familyKorNm=None, familyNm=None, fngsGnrlNm=None, fngsPilbkNo=None, genusKorNm=None, genusNm=None):
        # 과국명
        self.familyKorNm = familyKorNm
        # 과명
        self.familyNm = familyNm
        # 국명
        self.fngsGnrlNm = fngsGnrlNm
        # 도감번호
        self.fngsPilbkNo = fngsPilbkNo
        # 속국명
        self.genusKorNm = genusKorNm
        # 속명
        self.genusNm = genusNm


class Service:
    def __init__(self):
        self.base_url = 'http://openapi.nature.go.kr/openapi/service/rest/FungiService/'
        self.api_key = 'z87XiFqBjizhP7gRBLRttGzJYgKrESmLrKQNmb1aVULKjUTS9f6TBr2rppZBMSEXbq1ovC5bUdGj2N%2FYD6pKPg%3D%3D'

    def Test(self, st, sw, numOfRows, pageNo):
        url = self.base_url + '/fngsIlstrSearch?ServiceKey=' + self.api_key + '&st=' + st + '&sw=' + sw + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo
        # print(url)
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('resultCode').text
        resultMsg = root.find('resultCode').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                familyKorNm = item.find('familyKorNm').text
                familyNm = item.find('familyNm').text
                fngsGnrlNm = item.find('fngsGnrlNm').text
                fngsPilbkNo = item.find('fngsPilbkNo').text
                genusKorNm = item.find('genusKorNm').text
                genusNm = item.find('genusNm').text
                # results.append(
                #     Mushroom(familyKorNm=familyKorNm, familyNm=familyNm, fngsGnrlNm=fngsGnrlNm,
                #              fngsPilbkNo=fngsPilbkNo, genusKorNm=genusKorNm, genusNm=genusNm))

                results.append([familyKorNm, familyNm, fngsGnrlNm, fngsPilbkNo, genusKorNm, genusNm])

            return results
        else:
            print('오류발생코드', code)
            print('오류메세지', resultMsg)

        # html if 문 사용시 {% if data[0] =='송이버섯' %}

    def Test2(self, st, sw, numOfRows, pageNo):
        url = self.base_url + '/fngsIlstrSearch?ServiceKey=' + self.api_key + '&st=' + st + '&sw=' + sw + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('resultCode').text
        resultMsg = root.find('resultCode').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                familyKorNm = item.find('familyKorNm').text
                familyNm = item.find('familyNm').text
                fngsGnrlNm = item.find('fngsGnrlNm').text
                fngsPilbkNo = item.find('fngsPilbkNo').text
                genusKorNm = item.find('genusKorNm').text
                genusNm = item.find('genusNm').text
                results.append(Mushroom(familyKorNm=familyKorNm, familyNm=familyNm, fngsGnrlNm=fngsGnrlNm,
                             fngsPilbkNo=fngsPilbkNo, genusKorNm=genusKorNm, genusNm=genusNm))

                # results.append([familyKorNm, familyNm, fngsGnrlNm, fngsPilbkNo, genusKorNm, genusNm])

            return results
        else:
            print('오류발생코드', code)
            print('오류메세지', resultMsg)
