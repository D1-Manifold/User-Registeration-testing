from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

class UserCreate(BaseModel):
    email: str
    password: str
    confirm_password: str

@app.get('/')
def welcome():
    return 'Welcome to the Sai'

@app.post('/register')
def register(user: UserCreate):
    email = user.email
    password = user.password
    confirm_password = user.confirm_password

    # Validate email and password inputs
    if not email or not password or not confirm_password:
        raise HTTPException(status_code=400, detail='Please enter all required fields')
    if password != confirm_password:
        raise HTTPException(status_code=400, detail='Passwords do not match')

    # Check if email already exists in database
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_users WHERE email = %s", (email,))
    existing_user = cur.fetchone()
    cur.close()
    if existing_user:
        raise HTTPException(status_code=400, detail='Email already exists')

    # Store new user in database
    cur = conn.cursor()
    cur.execute("INSERT INTO test_users (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()
    cur.close()

    # Return success message
    return {'message': 'User created successfully'}
