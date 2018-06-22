from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friends2')


@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', all_friends=users)


@app.route('/add_friend', methods=['POST'])
def create():
	#Creates a mySql query that is passed to the database.
    query = "INSERT INTO users (first_name, last_name, occupation)VALUES(:first_name, :last_name, :occupation)"
    #creates a dictionary from the data in the request form. 
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)