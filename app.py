# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

##### DATABASE #####

def get_db_connection():
    host = "group7database.cb8giewg8z2a.us-east-1.rds.amazonaws.com"
    user = "admin"
    password = "GHpT>O0jemlG3i*[>9by*|E?KiEK"
    database = "CarRentalService"
    return pymysql.connect(host=host, user=user, password=password, database=database, cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello_world():
    myvar = 'INFR3810'
    return render_template('index.html', msg=myvar)

@app.route('/rollsroyce/')
def new_page1():
    return render_template('rollsroyce.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    PickUpLocation = request.form['PickUpLocation']

    # Insert data into RDS
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO Customer (name, email) VALUES (%s, %s)"
            sql = "INSERT INTO Location (PickUpLocation) VALUES (%s)"
            cursor.execute(sql, (name, email, PickUpLocation))
        connection.commit()
        connection.close()
        return "Reservation submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/bugatti/')
def new_page2():
    return render_template('bugatti.html')

@app.route('/infiniti/')
def new_page3():
    return render_template('infiniti.html')

@app.route('/lexus/')
def new_page4():
    return render_template('lexus.html')

@app.route('/list')
def list():
    db = Database()
    result = db.select()
    return render_template('results.html', result=result)
