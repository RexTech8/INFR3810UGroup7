# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

##### DATABASE #####

def get_db_connection():
    host = "group7database.cb8giewg8z2a.us-east-1.rds.amazonaws.com"
    user = "admin"
    password = "j>[1S1?4P~~|T)Et_8_1cFRgYgKp"
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
                                 password="j>[1S1?4P~~|T)Et_8_1cFRgYgKp",
                                 database="CarRentalService",
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Retrieve the Driver's License Number from the form
            ReservationID = request.form['license_number']

            # Execute the SQL query to fetch data based on the Driver's License Number
            sql = "SELECT * FROM Reservation JOIN Vehicle ON Reservation.ReservationID = Vehicle.VehicleID WHERE Reservation.ReservationID = %s;"
            cursor.execute(sql, (ReservationID))
            results = cursor.fetchall()

    finally:
        # Close the database connection
        connection.close()

    # Render the template with the search results
    return render_template('results.html', results=results)

@app.route('/delete', methods=['POST'])
def delete():
    # Connect to the database
    connection = pymysql.connect(host="group7database.cb8giewg8z2a.us-east-1.rds.amazonaws.com",
                                 user="admin",
                                 password="j>[1S1?4P~~|T)Et_8_1cFRgYgKp",
                                 database="CarRentalService",
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Retrieve the ReservationID to be deleted from the form
            ReservationID = request.form['reservation_id']
            # Execute the SQL query to delete data based on ReservationID
            sql = "DELETE FROM Reservation WHERE ReservationID = %s;"
            cursor.execute(sql, (ReservationID))

        with connection.cursor() as cursor:
            # Retrieve the ReservationID to be deleted from the form
            CustomerID = request.form['reservation_id']
            # Execute the SQL query to delete data based on ReservationID
            sql = "DELETE FROM Customer WHERE CustomerID = %s;"
            cursor.execute(sql, (CustomerID))

        with connection.cursor() as cursor:
            # Retrieve the ReservationID to be deleted from the form
            LocationID = request.form['reservation_id']
            # Execute the SQL query to delete data based on ReservationID
            sql = "DELETE FROM Location WHERE LocationID = %s;"
            cursor.execute(sql, (LocationID))

        with connection.cursor() as cursor:
            # Retrieve the ReservationID to be deleted from the form
            PaymentID = request.form['reservation_id']
            # Execute the SQL query to delete data based on ReservationID
            sql = "DELETE FROM Payment WHERE PaymentID = %s;"
            cursor.execute(sql, (PaymentID))

        with connection.cursor() as cursor:
            # Retrieve the ReservationID to be deleted from the form
            VehicleID = request.form['reservation_id']
            # Execute the SQL query to delete data based on ReservationID
            sql = "DELETE FROM Vehicle WHERE VehicleID = %s;"
            cursor.execute(sql, (VehicleID))
            
            # Commit the transaction
            connection.commit()

    finally:
        # Close the database connection
        connection.close()

    # Redirect back to the index page or any other page
    return "Reservation deleted successfully!"



# Route to handle form submission and modify reservation
@app.route('/modify', methods=['POST'])

    
def modify_reservation():
    connection = pymysql.connect(host="group7database.cb8giewg8z2a.us-east-1.rds.amazonaws.com",
                                 user="admin",
                                 password="j>[1S1?4P~~|T)Et_8_1cFRgYgKp",
                                 database="CarRentalService",
                                 cursorclass=pymysql.cursors.DictCursor)
    # Retrieve form data
    reservation_id = request.form['reservation_id']
    new_start_date = request.form['start_date']
    new_end_date = request.form['end_date']
    new_cost = request.form['cost']

    try:
        with connection.cursor() as cursor:
            # Execute SQL query to update reservation
            sql = "UPDATE Reservation SET StartDate = %s, EndDate = %s, Cost = %s WHERE ReservationID = %s"
            cursor.execute(sql, (new_start_date, new_end_date, new_cost, reservation_id))
        
        # Commit the transaction
        connection.commit()

        # Redirect to a success page or render a success message
        return "Reservation modified successfully!"

    except Exception as e:
        # Handle any exceptions
        return f"An error occurred: {str(e)}"

    finally:
        # Close the database connection
        connection.close()


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

@app.route('/reservations/')
def newpage6():
    return render_template('reservations.html')

@app.route('/results/')
def newpage7():
    return render_template('results.html')

@app.route('/modify/')
def newpage8():
    return render_template('modify.html')