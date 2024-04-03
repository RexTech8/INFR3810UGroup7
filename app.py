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
    CustomerID = request.form['license']
    name = request.form['name']
    address = request.form ['address']
    email = request.form['email']
    phone = request.form['phone']
    DriversLicenseNumber = request.form['license']

    LocationID = request.form['license']
    PickUpLocation = request.form['pickup']
    DropOffLocation = request.form['dropoff']

    PaymentID = request.form["license"]
    Date = request.form['date']
    Method = request.form['method']

    VehicleID = request.form['license']
    Make = request.form['make']
    Model = request.form['model']
    LicensePlateNumber = request.form['license_plate']
    Rate = request.form['rate']

    ReservationID = request.form['license']
    StartDate = request.form['start_date']
    EndDate = request.form['end_date']
    Cost = request.form['rate']

    # Insert data into RDS
    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:
            sql_customer = "INSERT INTO Customer (CustomerID, name, address, email, PhoneNumber, DriversLicenseNumber) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_customer, (CustomerID, name, address, email, phone, DriversLicenseNumber))

        with connection.cursor() as cursor:
            sql_loc = "INSERT INTO Location (LocationID, PickUpLocation, DropOffLocation) VALUES (%s, %s, %s)"
            cursor.execute(sql_loc, (LocationID, PickUpLocation, DropOffLocation))

        with connection.cursor() as cursor:
            sql_pay = "INSERT INTO Payment (PaymentID, Date, Method) VALUES (%s, %s, %s)"
            cursor.execute(sql_pay, (PaymentID, Date, Method))

        with connection.cursor() as cursor:
            sql_vehicle = "INSERT INTO Vehicle (VehicleID, Make, Model, LicensePlateNumber, Rate) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_vehicle, (VehicleID, Make, Model, LicensePlateNumber, Rate))

        with connection.cursor() as cursor:
            sql_reservation = "INSERT INTO Reservation (ReservationID, StartDate, EndDate, Cost) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_reservation, (ReservationID, StartDate, EndDate, Cost))


        connection.commit()
        connection.close()
        return "Reservation submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/search', methods=['POST'])
def search():
    # Connect to the database
    connection = pymysql.connect(host="group7database.cb8giewg8z2a.us-east-1.rds.amazonaws.com",
                                 user="admin",
                                 password="GHpT>O0jemlG3i*[>9by*|E?KiEK",
                                 database="CarRentalService",
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Retrieve the Driver's License Number from the form
            ReservationID = request.form['license_number']

            # Execute the SQL query to fetch data based on the Driver's License Number
            sql = "SELECT * FROM Reservation WHERE DriversLicenseNumber = %s"
            cursor.execute(sql, (ReservationID))
            results = cursor.fetchall()

    finally:
        # Close the database connection
        connection.close()

    # Render the template with the search results
    return render_template('index.html', results=results)



@app.route('/bugatti/')
def new_page2():
    return render_template('bugatti.html')

@app.route('/infiniti/')
def new_page3():
    return render_template('infiniti.html')

@app.route('/lexus/')
def new_page4():
    return render_template('lexus.html')

@app.route('/form/')
def newpage5():
    return render_template('form.html')
