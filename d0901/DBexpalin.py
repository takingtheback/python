import platform
# 파이썬 사용하는 버전 체크
print(platform.architecture())

"""
ctrl + alt + del 후 
service -> oracle 3가지 항목 실행되는지 체크
- OracleServiceXe
- OracleXeClrAgent
- OracleXETNSListener

download 
- Basic Light Package
https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html

path 추가 
내컴퓨터 -> 속성 -> 고급 환경변수 
C:\instantclient_19_12 추가 후 맨위설정

파이참 하단부 터미널
pip install cx_oracle
"""

"""
db 구문

select table_name from tabs;

drop table test;

create table test(
num number primary key,
name varchar2(20),
price number,
disc varchar2(100)
);

create sequence seq_test;

select * from test;

delete test;

commit;

create table product(
num number primary key,
name varchar2(20) not null,
price number not null,
amount number
);

create sequence seq_product;

select * from product;
"""