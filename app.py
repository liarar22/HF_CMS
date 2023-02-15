# extension에서 flask 설치하고, terminal에 pip install flask
# 인식 못하는 라이브러리가 있다면 pip 명령어를 활용해서 install
import os #절대경로 지정 위함
from flask import Flask
from flask import render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cjsak753'
app.config['MYSQL_DB'] = 'hf_cms_accounts'

mysql = MySQL(app)

app.secret_key = '123123'

@app.route(rule = '/')
def HF_CMS_01():
    return render_template(template_name_or_list = 'logo_page.html')

@app.route(rule = '/login', method = ['get', 'POST'])
def login():
    if request.method == 'post':
        username = request.form['id']
        password = request.form['pw']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM hf_cms_accounts WHERE id = %s", (id,))
        user = cur.fetchone()
        cur.close

        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))

        else:
            error = 'Invaild username or password'
            return render_template('login_page.html', error=error)
    
    return render_template('login_page.html')

def dashboard():
    if 'user_id' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM hf_cms_accounts WHERE username = %s", (session['user_id'],))
        user = cur.fetchone()
        cur.close()

        return render_template('logo_page.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


#def HF_CMS_02():
#   return render_template(template_name_or_list = 'login_page.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
