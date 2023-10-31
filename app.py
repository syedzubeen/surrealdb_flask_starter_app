from flask import Flask, render_template, request, redirect, url_for, session
from surrealdb import Surreal

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a secret key for session management


# Define SurrealDB connection settings
SURREALDB_WS_URL = "ws://localhost:8000" 

async def insert_user_into_surreal(username, password):
    async with Surreal(SURREALDB_WS_URL) as db:
      
        await db.use("test1", "test1") 

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

        return redirect(url_for('welcome'))  


    return render_template('index.html')

@app.route('/welcome', methods=['POST', 'GET'])
async def welcome():
    # Get the username from the session variable
    username = session.get('username')
    
    message = ""  # Initialize the message variable


    if request.method == 'POST':
        if 'delete-profile' in request.form:  # Check if the "Delete Profile" button was clicked
            if await delete_user_profile(username):
                message = "Profile deleted successfully."
            else:
                message = "Profile deletion failed."
        
        else:  
            
        # Create an empty dictionary to store the fields to update
            update_fields = {
            "sex": "Male"  # temporarily Hardcoded to "Male"
            }

            # Fields from the form that might be empty or skipped
            fields_to_check = ['age', 'state', 'country', 'address']

            # Iterate over the fields and add them to the update dictionary if they exist in the form data
            for field in fields_to_check:
                value = request.form.get(field)  # Use request.form.get to avoid KeyError
                if value is not None:
                    update_fields[field] = value

            app.logger.info("Values: " + str(update_fields))
            updated_specific_user = "person:"+username
            db = Surreal("http://localhost:8000")
            await db.connect()
            #await db.signin({"user": "admin", "pass": "admin"})
            await db.use("test1", "test1")
            await db.update(updated_specific_user, update_fields)

    return render_template('welcome.html', username=username)

async def delete_user_profile(username):
    person_id= "person:"
    try:
        print ("trying to DELETE PROFILE****")
        db = Surreal("http://localhost:8000")
        await db.connect()
        await db.use("test1", "test1")
        record_to_delete = "DELETE FROM person WHERE user = '" + username + "';"
        await db.query(record_to_delete)
        
        #await db.delete(person_id)
        return True  # Profile deletion was successful
    except Exception as e:
        print("Profile deletion failed:", str(e))
        return False  # Profile deletion failed

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/user_info', methods=['GET', 'POST'])
def user_info():
     
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Fetch the password from the form
        
    
    # Render the "user_info.html" template and pass the username 
        return render_template('user_info.html', username=username)
    
    # If it's a GET request, render the initial form for logging in
    return render_template('user_info_form.html')