from flask import Flask, render_template, request, redirect, url_for, session
from surrealdb import Surreal



app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a secret key for session management


# Define SurrealDB connection settings
SURREALDB_WS_URL = "ws://localhost:8000" 

async def insert_user_into_surreal(username, password):
    async with Surreal(SURREALDB_WS_URL) as db:
      
        await db.use("test1", "test1")  # Replace with your database and collection name

        # Create a new user
        await db.create(
            "person",
            {
                "user": username,   
                "pass": password,
            },
        )


@app.route('/', methods=['GET', 'POST'])
async def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        await insert_user_into_surreal(username, password)  # Insert the user into SurrealDB

         # Store the username in a session variable
        session['username'] = username

        return redirect(url_for('welcome'))  # Redirect to the welcome page


    return render_template('index.html')

@app.route('/welcome')
def welcome():
    # Get the username from the session variable
    username = session.get('username')
    if username:
        return f'Welcome, {username}!'
    else:
        return 'Welcome!'
    

if __name__ == '__main__':
    app.run(debug=True)
