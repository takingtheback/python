from flask import Flask, request, render_template, redirect
import models.factory as model
import prod_route as pr

import config

 #모델 파일에 만든 객체 불러옴
db = model.db
migrate = model.migrate

app = Flask(__name__)
app.config.from_object(config)  #플라스크 컨피그에 사용자정의 컨피그 추가
app.register_blueprint(pr.bp)

# ORM
db.init_app(app)
migrate.init_app(app, db)

service = model.Service()

@app.route('/')
def root():
    plist = service.getAll()
    return render_template('index.html', plist=plist)

@app.route('/add')
def add():
    service.addProduct()
    return redirect('/')

if __name__ == '__main__':
    app.run()#flask 서버 실행