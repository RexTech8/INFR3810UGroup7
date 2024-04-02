# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

##### DATABASE #####

class Database:
    def __init__(self):
        host = "YOURUSERNAME.mysql.pythonanywhere-services.com"
        user = "YOURUSERNAME"
        pwd = "YOURMYSQLPASSWORD"
        db = "YOURDATABASENAME"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    #SQL
    def select(self):
        self.cur.execute("SELECT * FROM Customer")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def insert(self, id, name, grade):
        self.cur.execute("INSERT INTO Customer ((CusotmerID, Name, Address, Email, PhoneNumber, DriversLicenseNumber) VALUES(%s, %s, %s, %s, %s, $s)"), (id, name, grade, address, email, phonenumber, driverslicensenumber))
        self.con.commit()
        self.con.close()

        return "OK"

    def update(self, Name, Address, Email, PhoneNumber, DriversLicenseNumber):
        self.cur.execute ("UPDATE Customer SET Name=%s, Address=%s, Email=%s, PhoneNumber=%s, DriversLicenseNumber=%s")
        self.con.commit()
        self.con.close()

        return "Updated"

    def delete_entity(self, id):
        self.cur.execute("DELETE FROM Customer WHERE CusotmerID=?, Name=?, Address=?, Email=?, PhoneNumber=?, DriversLicenseNumber=?"), (CusotmerID, Name, Address, Email, PhoneNumber, DriversLicenseNumber))
        self.con.commit()
        self.con.close()
        
        return "Deleted"


@app.route('/')
def hello_world():
    myvar = 'INFR3810'
    return render_template('index.html', msg=myvar)

@app.route('/rollsroyce/')
def new_page1():
    return render_template('rollsroyce.html')

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
