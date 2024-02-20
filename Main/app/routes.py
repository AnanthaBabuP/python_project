from app import app
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # # Check if the username exists and the password matches
        # if username in users and users[username] == password:
        #     return redirect(url_for('success'))
        # else:
        #     return render_template('login.html', message='Invalid username or password')

         # Check if the username exists and the password matches
        cursor = db.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        print(user)

        if user and user[0] == password:
            return redirect(url_for('success'))
        else:
            return render_template('login.html', message='Invalid username or password')

    return render_template('login.html', message='')

@app.route('/success')
def success():
    return 'Login Successful'

if __name__ == '__main__':
    app.run(debug=True)