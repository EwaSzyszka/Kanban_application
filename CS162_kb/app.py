from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/ewa_anna_szyszka/Desktop/CS162_kb/sample.db'
#connect = sqlite3.connect('sample.db')
#db.SQLAlchemy(app)

#class ExampleTable(db.Model):
#    id = db.Column(db.Integer,primary_key= True)

@app.route('/')
def index():
    return render_template("kambanboard.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=['POST'])
def add():
    return ('222') 


#@app.route('/add', methods=['POST'])
#def add():
#    todo = Todo(text=request.form['todoitem'], complete=False)
#    db.session.add(todo)
#    db.session.commit()

#    return redirect(url_for('index'))'''

if __name__ == '__main__':
    app.run(debug=True)
