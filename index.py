from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)
#configure
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='schema'
mysql=MySQL(app)

app.secret_key='mysecretkey'

@app.route('/')
def home ():
    return render_template("home.html")

@app.route('/pago')
def pago():
    cur=mysql.connection.cursor()      #connection oracle
    cur.execute('SELECT * FROM usuarios')
    data=cur.fetchall()
    return render_template("pagos.html",usuarios=data)



@app.route('/nc')
def nc():
     return  render_template("nc.html")

@app.route('/clientes')
def clientes():
     return render_template("clientes.html")


if __name__ == "__main__":
     app.run(debug=True)