# extension에서 flask 설치하고, terminal에 pip install flask
# 로그인 정보 db 연동을 위해 terminal에 pip install flask-mysqldb
# https://streamls.tistory.com/entry/Flask%EA%B0%95%EC%A2%8C-%EB%A1%9C%EA%B7%B8%EC%9D%B8 : 로그인 방법 관련해서 이걸 챙겨보자
from flask import Flask, render_template

app = Flask(__name__)

@app.route(rule = '/')
def HF_CMS_01():
    return render_template(template_name_or_list = 'logo_page.html')

@app.route(rule = '/login')
def HF_CMS_02():
    return render_template(template_name_or_list = 'login_page.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
