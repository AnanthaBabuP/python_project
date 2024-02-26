# from app import app
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import mysql.connector
import bcrypt
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass@my_sql01'
app.config['MYSQL_DB'] = 'user'

# Connect to MySQL
db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

def validate_registration(username, email, password):
    """
    Validate user registration data:
    - Username must be alphanumeric and between 5 and 20 characters.
    - Email must be in a valid format.
    - Password must be at least 8 characters long.
    """
    if not username.isalnum() or len(username) < 5 or len(username) > 20:
        return False
    if '@' not in email or '.' not in email:
        return False
    if len(password) < 8:
        return False
    return True

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login')
def loginIndex():
    return render_template('login.html', title='Home')
# Dummy user data (replace this with your actual user authentication mechanism)
# users = {
#     'john': 'password123',
#     'jane': 'password456'
# }

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/register')
def show_register():
    return render_template('register.html',message='')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        message = []
        if(username == ''):
            message.append("Enter UserName")
            return render_template('login.html', message='Enter UserName')
        elif(password == ''):
            message.append("Enter Password") 
            return render_template('login.html', message='Enter Password')

        if(len(message) > 0):
            print(len(message))

        # Without DB Connection

        # # Check if the username exists and the password matches
        # if username in users and users[username] == password:
        #     return redirect(url_for('success'))
        # else:
        #     return render_template('login.html', message='Invalid username or password')

         # Check if the username exists and the password matches
        
        # With DB Connect Codes
        cursor = db.cursor()
        cursor.execute("SELECT username,password,id FROM user_info WHERE username = %s", (username,))
        users = cursor.fetchall()
        if users:
            for user in users:
                print(user)
                # Hash the password
                stored_password = user[1]  # Retrieve the hashed password from the database
                # Print the hashed password
                # Verify the provided password with the stored hashed password
                if verify_password(password, stored_password):
                    print("Password Matched! User Authenticated.")
                    return render_template('success.html', employee_id=user[2], screen = "Login")
                else:
                    print("Invalid Password! Authentication Failed.")

        return render_template('login.html', message='Invalid username or password')


# Function to hash a password
def hash_password(password):
    # Generate a random salt and hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

# Function to verify a password
def verify_password(input_password, hashed_password):
    # Check if the input password matches the hashed password
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Validate registration data
        if not validate_registration(username, email, password):
            return render_template('register.html', message='Invalid registration data')


        # Add code to insert username and password into your database
        mycursor = db.cursor()
        sql = "INSERT INTO user_info (username, email, password ) VALUES (%s, %s, %s)"
        val = (username, email, password)
        mycursor.execute(sql, val)
        db.commit()

        cursor = db.cursor()
        cursor.execute("SELECT id FROM user_info WHERE username = %s and password = %s and email = %s", (username,password,email))
        user = cursor.fetchone()
        print("username! ", username, "Pass : ",password)
        return render_template('success.html', employee_id = user[0], screen = "Register")


@app.route('/detail', methods=['POST'])
def detail_view():
     if request.method == 'POST':
        id = request.form['id']
        cursor = db.cursor()
        cursor.execute("SELECT u.*, d.* FROM user_info u LEFT JOIN user_details d ON u.id = d.id WHERE u.id = %s", (id,))
        user = cursor.fetchone()
        if user:
            return render_template('user_detail.html', user=user,message="")
        else:
            return "User not found"

@app.route('/edit_detail', methods=['POST'])
def detail_view_edit():
     if request.method == 'POST':
        id = request.form['userId']
        cursor = db.cursor()
        cursor.execute("SELECT u.*, d.* FROM user_info u LEFT JOIN user_details d ON u.id = d.id WHERE u.id = %s", (id,))
        user = cursor.fetchone()
        if user:
            return render_template('user_detail_edit.html', user=user,error= [])
        else:
            return "User not found"

@app.route('/update_detail', methods=['POST'])
def update_detail():
     if request.method == 'POST':
        id = request.form['userId']
        userName = request.form['username']
        email = request.form['email']
        address = request.form['address']
        contact = request.form['contact']
        description = request.form['description']
        join_date = request.form['join_date']
        gender = request.form['gender']
        user = []

        # Append values to the list at specific positions
        user.extend([None] * 11) 
        user[4] = id
        user[0] = userName
        user[1] = email
        user[6] = address

        user[7] = contact
        user[8] = description
        user[9] = join_date
        user[10] = gender

        print(request.form)
        message = []
        
        if email == 'None' or email == '':
            message.append("Please Enter Email ")
        if address == 'None' or address == '':
            message.append("Please Enter Address")
        if contact == 'None' or contact == '':
            message.append("Please Enter Contact")
        if description == 'None' or description == '':
            message.append("Please Enter Description")
        if join_date == 'None' or join_date == '':
            message.append("Please Enter Join Date")
        if gender == 'None' or gender == '':
            message.append("Please Select Gender")

        if len(message) > 0 :
            return render_template('user_detail_edit.html', user=user,messages= message)
        
        # Parse the date string into a datetime object
        date_object = datetime.strptime(join_date, "%Y-%m-%d")

        # Format the datetime object into yyyymmdd format
        formatted_date = date_object.strftime("%Y%m%d")

        print(formatted_date)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_info WHERE id = %s", (id,))
        val = cursor.fetchone()
        if val[0] != userName or  val[1] != email:
                print("Inside User Info")
                update_query = "UPDATE user_info SET username = %s ,email = %s WHERE id = %s"
                cursor.execute(update_query, (userName, email, id))

        cursor.execute("SELECT * FROM user_details WHERE id = %s", (id,))
        user = cursor.fetchone()
        if user:
            update_query = "UPDATE user_details SET address = %s, contact_no = %s, description = %s, DOJ = %s, gender = %s  WHERE id = %s"
            cursor.execute(update_query, (address, contact, description, join_date, gender, id))
            result = "User details updated successfully."
           
        else:
            # User doesn't exist, insert new record
            insert_query = "INSERT INTO user_details (id, address, contact_no, description, DOJ, gender) VALUES (%s, %s,%s, %s,%s, %s)"
            cursor.execute(insert_query, (id, address, contact, description, formatted_date, gender))
            result = "New user details inserted successfully."
        db.commit()
        cursor.execute("SELECT u.*, d.* FROM user_info u LEFT JOIN user_details d ON u.id = d.id WHERE u.id = %s", (id,))
        user = cursor.fetchone()
        return render_template('user_detail.html', user=user, message=result)

@app.route('/detail_back', methods=['POST'])
def detail_back():
    userId = request.form['userId']
    return render_template('success.html', employee_id = userId, screen = "Login")

@app.route('/logout')
def logout():
   return render_template('login.html', title='Home')

if __name__ == '__main__':
    app.run(debug=False)