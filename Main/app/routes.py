# from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
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
                if user[0] == username and user[1] == password:
                    return render_template('success.html', employee_id=user[2], screen = "Login")
        return render_template('login.html', message='Invalid username or password')

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
            return render_template('user_detail.html', user=user)
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
            return render_template('user_detail_edit.html', user=user)
        else:
            return "User not found"

@app.route('/update_detail', methods=['POST'])
def update_detail():
     if request.method == 'POST':
        id = request.form['userId']
        cursor = db.cursor()
        cursor.execute("SELECT u.*, d.* FROM user_info u LEFT JOIN user_details d ON u.id = d.id WHERE u.id = %s", (id,))
        user = cursor.fetchone()
        if user:
            return render_template('user_detail_edit.html', user=user)
        else:
            return "User not found"

if __name__ == '__main__':
    app.run(debug=False)