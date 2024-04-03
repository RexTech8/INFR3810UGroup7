# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

##### DATABASE #####

class Database:
    def __init__(self):
        host = "group7database.cb8giewg8z2a.us-east-1.rds.amazonaws.com"
        user = "admin"
        pwd = "GHpT>O0jemlG3i*[>9by*|E?KiEK"
        db = "group7database"

        self.con = pymysql.connect(host=host, user=user, password=pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def insert_booking(self, pickup, return_date, name, address, email, phone, license):
        sql = "INSERT INTO Booking (PickUpDate, ReturnDate, FullName, Address, Email, Phone, DriversLicense) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(sql, (pickup, return_date, name, address, email, phone, license))
        self.con.commit()

@app.route('/')
def hello_world():
    myvar = 'INFR3810'
    return render_template('index.html', msg=myvar)

@app.route('/rollsroyce/')
def new_page1():
    pickup = request.form['PickUp']
    return_date = request.form['Return']
    name = request.form['Name']
    address = request.form['Address']
    email = request.form['Email']
    phone = request.form['Phone']
    license = request.form['Licence']
    db = Database()
    db.insert_booking(pickup, return_date, name, address, email, phone, license)
    return ('rollsroyce.html')

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

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    msg = ""
    if request.method == "POST":
        data = request.form
        id = data['CusomterID']
        name = data['Name']
        grade = data['Address']
        email = data['Email']
        phonenumber = data['PhoneNumber']
        driverslicensenumber = data['DriversLicenseNumber']

        db = Database()
        msg = db.insert(id, name, grade)



    return render_template('form.html', msg=msg)
