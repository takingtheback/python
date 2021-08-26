"""
# 객체 지향 프로그래밍(중,대형)
순차적프로그래밍은 시간의 흐름 순서대로 코드를 짰다면 객체 지향 프로그래밍은 객체를 중심으로 개발.
객체를 정의하고 객체와 객체 사이의 관계를 정의하는 방식으로 프로그래밍을 한다.

객체 : 세상을 프로그램으로 모델링할 때, 모델링의 대상이 되는 사람이나 사물, 개념, 즉 샘플.
객체를 샘플링
atm
기능정의
입금
출금
1.카드를 넣는다
2. 카드 비밀번호 입력
3. 출금금액 입력
4. 카드 연결 계좌 조회
5. yes : 계좌 출력
no : 메세지 출력
조회
이체

"""
# class Card:
#     def __init__(self): # 생성자
#         self.number = ''
#         self.pwd = ''
#         self.date = ''
#         self.account = None
#
#     def printInfo(self): # 메서드
#         print(self.number)
#         print(self.pwd)
#         print(self.date)
#         print(self.account)
#
#
# c1 = Card()
# c1.number = '1234 - 3456 - 4567'
# c1.pwd = '1234'
# c1.date = '03/24'
# c1.account = '23456789'
#
# c1.printInfo()


class Card:
    def __init__(self, number='', pwd=None, date=None, account=None): # 생성자
        self.number = number
        self.pwd = pwd
        self.date = date
        self.account = account

    def printInfo(self): # 메서드
        print(self.number)
        print(self.pwd)
        print(self.date)
        print(self.account)


c1 = Card(number='1234 - 3456 - 4567')
c1.printInfo()
print(c1)
c2 = Card(number='1234 - 3456 - 4567', pwd='4321')
c2.printInfo()
print(c2)