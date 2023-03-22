from flask import Flask, request, redirect, url_for, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

@app.route('/Welcome', methods=['GET', 'POST'])
def welcome():
    return 'Welcome to the Sai'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        email = request.json.get('email')
        password = request.json.get('password')
        confirm_password = request.json.get('confirm_password')
        
        # Validate email and password inputs
        if not email or not password or not confirm_password:
            return 'Please enter all required fields'
        if password != confirm_password:
            return 'Passwords do not match'
        
        # Check if email already exists in database
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_users WHERE email = %s", (email,))
        existing_user = cur.fetchone()
        cur.close()
        if existing_user:
            return 'Email already exists'
        
        # Store new user in database
        cur = conn.cursor()
        cur.execute("INSERT INTO test_users (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
        cur.close()
        
        # Redirect to welcome page
    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)    