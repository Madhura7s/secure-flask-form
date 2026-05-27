from flask import Flask, render_template, request, redirect, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect

import re
import bcrypt
import sqlite3

app = Flask(__name__)

csrf = CSRFProtect(app)

limiter = Limiter(
    get_remote_address,
    app=app
)

app.secret_key = 'Madhura_Secure_Flask_Project_2026_!@#'

def get_db_connection():

    conn = sqlite3.connect('users.db')

    conn.row_factory = sqlite3.Row

    return conn

def create_table():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            student_id TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL

        )

    ''')

    conn.commit()

    conn.close()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

#Login Page Route
@app.route('/login')
@limiter.limit("10 per minute")
def login_page():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')

    password = request.form.get('password')

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(

        '''

        SELECT * FROM users
        WHERE email = ?

        ''',

        (email,)
    )

    user = cursor.fetchone()

    conn.close()


    # User Exists?
    if user:

        stored_password = user['password']

        password_match = bcrypt.checkpw(
            password.encode('utf-8'),
            stored_password.encode('utf-8')
        )

        if password_match:

            # Create Session
            session['user_email'] = user['email']

            return redirect('/dashboard')


    return "Invalid Email or Password"

@app.route('/dashboard')
def dashboard():

    # Check Session
    if 'user_email' not in session:

        return redirect('/login')

    return f"""

    <h1>Welcome</h1>

    Logged In As:
    {session['user_email']}

    <br><br>

    <a href="/logout">
        Logout
    </a>

    """

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

# Form Submission
@app.route('/submit', methods=['POST'])
@limiter.limit("5 per minute")
def submit():

    # Get Form Data
    name = request.form.get('name')
    student_id = request.form.get('student_id')
    email = request.form.get('email')
    password = request.form.get('password')

    # -------------------------
    # NAME VALIDATION
    # -------------------------

    name_pattern = r"^[A-Za-z ]+$"

    if not re.match(name_pattern, name):
        return "Invalid Name"


    # -------------------------
    # ID VALIDATION
    # -------------------------

    if not student_id.isdigit():
        return "ID Must Be Numeric"


    # -------------------------
    # EMAIL VALIDATION
    # -------------------------

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_pattern, email):
        return "Invalid Email"


    # -------------------------
    # PASSWORD VALIDATION
    # -------------------------

    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'

    if not re.match(password_pattern, password):
        return """
        Weak Password <br><br>

        Password Must Contain:
        <br>
        - Uppercase Letter
        <br>
        - Lowercase Letter
        <br>
        - Number
        <br>
        - Minimum 8 Characters
        """


    # -------------------------
    # PASSWORD HASHING
    # -------------------------

    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )

    # -------------------------
    # DATABASE INSERT
    # -------------------------

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(
            '''

            INSERT INTO users
            (name, student_id, email, password)

            VALUES (?, ?, ?, ?)

            ''',

            (
                name,
                student_id,
                email,
                hashed_password.decode('utf-8')
            )
        )

        conn.commit()

    except sqlite3.IntegrityError:

        conn.close()

        return "Email Already Exists"

    conn.close()

    # -------------------------
    # SUCCESS RESPONSE
    # -------------------------

    return f"""

    <h2>Registration Successful</h2>

    Name: {name}<br>
    ID: {student_id}<br>
    Email: {email}<br><br>

    Password Stored Securely<br><br>

    Hashed Password:<br>
    {hashed_password.decode('utf-8')}

    """

# Run Server
if __name__ == '__main__':

    create_table()

    app.run(debug=True)
