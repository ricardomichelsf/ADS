import os
from flask import Flask, request, render_template
from sqlalchemy import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configuração
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Framework'
app.config['MYSQL_DATABASE_DB'] = 'dados'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():
    return render_template('singup.html')

@app.route('/signup', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    if nome and email and senha:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("inserir into aula_mvc (user_name, user_username, passwoard) VALUES (%s, %s, %s)", ( nome, email, senha))
        conn.commit()
    return render_template('singup.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
