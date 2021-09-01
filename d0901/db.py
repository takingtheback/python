import cx_Oracle


# vo
class Test:
    def __init__(self, num=None, name=None, price=None, desc=None):
        self.num = num
        self.name = name
        self.price = price
        self.desc = desc

    def print(self):
        print('num:', self.num, '/ name:', self.name, '/ price:', self.price, '/ descript:', self.desc)


"""
# db 작업 절차
1. db 커넥션 수립
2. 커서 객체 생성
3. sql 구문 작성
4. 바인딩 변수 처리
5. sql 실행
6. 커밋
    - 쓰기: 커밋
    - 읽기: 검색 결과 -> vo -> list
7. 커넥션 클로즈
"""
class Dao_test:
    def select_all(self):
        conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'select * from test'
        cursor.execute(sql)
        datas = []
        for row in cursor:
            datas.append(Test(row[0], row[1], row[2], row[3]))
        conn.close()
        return datas

    def select(self, num):
        conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'select * from test where num=:1'
        d = (num,)
        cursor.execute(sql, d)
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            return Test(row[0], row[1], row[2], row[3])

    def insert(self, t):
        # 1단계 커넥션 수립
        conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        # 커서 객체 생성. db 작업(쿼리문 실행 api 제공, 검색 결과도 담는 객체)
        cursor = conn.cursor()
        # jdbc ? 와 같은 효과 :1, :2 ...
        sql = 'insert into test values(seq_test.nextval, :1, :2, :3)'
        d = (t.name, t.price, t.desc)   # 바인딩 변수에 할당한 값을 튜플에 저장
        cursor.execute(sql, d)          # sql 문 실행
        # cursor.execute(sql)           # sql 문 실행(바인딩 변수가 없는 경우)
        conn.commit()                   # 쓰기 완료: db commit
        conn.close()

    def update(self, t):
        conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'update test set price=:1, disc=:2 where num=:3'
        d = (t.price, t.desc, t.num)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()


def main():
    dao = Dao_test()
    dao.insert(Test(1, 'aaa', 1000, 'info1'))
    dao.insert(Test(2, 'bbb', 2500, 'info2'))
    dao.insert(Test(3, 'ccc', 1500, 'info3'))
    # dao.update(Test(11, '', 2500, '가나다'))
    datas = dao.select_all()
    for t in datas:
        t.print()


main()
