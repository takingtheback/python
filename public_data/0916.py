import requests
"""
# vo / dto : 값을 담는 객체, 캡슐화, 생성자에 멤버변수 정의하면 끝
# self(현재 객체의 참조값) == java의 this(현재 객체의 참조값)
# 모든 멤버변수와 메서드 사용시 앞에 self
# 파이썬은 스크립트 언어라서 한줄씩 실행되므로, 컴파일 언어처럼 전체 구조 활용 불가

class Bus {
    private String route_id;
    private String bus_name;

    public Bus() {}
    public Bus(Sting route_id) {
        this.route_id = route_id
    }
    public Bus(Sting bus_name) {
        this.bus_name = bus_name
    }
    
"""


class Bus:
    def __init__(self, route_id=None, bus_name=None):
        self.route_id = route_id
        self.bus_name = bus_name


b = Bus('1234')

