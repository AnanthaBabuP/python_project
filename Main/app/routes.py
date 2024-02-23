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
    return render_template('register.html')

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
        else:
            return render_template('login.html', message='Invalid username or password')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
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

# @app.route('/success')
# def success():
#     return 'Login Successful'

@app.route('/detail')
def detail_view():
     if request.method == 'POST':
         id = request.form['id']
         print(id)

if __name__ == '__main__':
    app.run(debug=False)