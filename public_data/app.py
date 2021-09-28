from flask import Flask, render_template
from public_data.routes import routes as r
import threading

app = Flask(__name__)

#블루 프린트 등록
app.register_blueprint(r.bp)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Timer(60, app.run(port=5000)).start()
