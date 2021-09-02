from flask import Flask, render_template
import routes.member_route as mr


app = Flask(__name__)  # 웹 어플리케이션 객체 생성

app.register_blueprint(mr.bp)


@app.route('/')
def root():
    return render_template('index.html', msg='MMS python')


if __name__ == '__main__':
    app.run()  # flask 서버 실행
