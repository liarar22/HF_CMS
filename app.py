# extension에서 flask 설치하고, terminal에 pip install flask
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
