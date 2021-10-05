from flask import Flask, request, render_template, redirect, session
import service as s

#플라스크 객체 생성
app = Flask(__name__)

service = s.Service()

@app.route('/')
def root():
    return render_template('form.html')

@app.route('/grade', methods=['POST'])
def grade():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    res = service.getResult2(s.Wine(a,b,c,d))
    return '와인 등급은 '+str(res)+' 입니다'


if __name__ == '__main__':
    app.run()#flask 서버 실행