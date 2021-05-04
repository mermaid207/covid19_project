from flask import Flask, render_template
import covid19
import covid19_openapi

# 플라스크 앱 생성
app = Flask(__name__)

# URL 라우터 설정
@app.route('/')
def index():
    data = covid19.get_corona_summary()
    city_data = covid19_openapi.get_city_data()

    return render_template('index.html', corona_data=data, corona_city=city_data)

# 메인 코드
if __name__ == "__main__":
    app.run(debug=True)

