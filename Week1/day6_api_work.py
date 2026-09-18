 
#NOTE - Insutructions:
# we are going to practice / study web framework and creating APIs & Databases
# so we r using python so to talk to said DB we are going to be using "SQLAlechemy" which is a python library that allows us to talk to the DB in a more pythonic way (instead of raw SQL)
# Than we r going to use web framework like Flask, DJango, FASTapi, ETC all we r going to do is call it and create instance 


# libraries we r going to use
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy


# create flask instace 
app = Flask(__name__)

# this is our Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # this is the path to the database file
db = SQLAlchemy(app)  # this is the instance of the database


#SECTION - USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # so a user has an ID that is an int
    name = db.Column(db.String(80), unique=True, nullable=False) # user has name, where its a string, unique, and 80 characters long, and cannot be null
    email = db.Column(db.String(120), unique=True, nullable=False) # user has email, where its a string, unique, and 120 characters long, and cannot be null
    
    
    # return these exactly values into a dictionary when user is created 
    def to_dict(self):
        return {
            "user_id": self.id,
            "user_name": self.name,
            "user_email": self.email
        }
        
        
    
# we are now going to create routes for said user, API routes, so we can create a user, get a user, update a user, delete a user, and get all users. Theser are what APIs are usually for. 
# we have an obkect "user" and we want to be able to create, read, update, and delete (CRUD) that object. So we will create routes for each of those actions.

@app.route('/users', methods = ['POST'])
def create_user():
    
    # this is asking for the data in the request body, checks if the data is valid. Needs to have a name and email, if not return an error. If valid, create a new user object and add it to database 
    data = request.get_json() 
    
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Missing name or email"}), 400
    
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()

    # add the user to the database and return the user as a dictionary with a 201 status code
    return jsonify(user.to_dict()), 201




@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # this goes into the db sessions and grabs the user with the given id, if it exists return the user as a dictionary, if not return an error
    # looking in the User table where ID is x...
    user = db.session.get(User, user_id) # looking in the User table where ID is x to look in that tbale is "user_id" 
    
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404




@app.route("/users", methods = ['GET'])
def get_all_users():
    
    users = User.query.all()  # this is a query to get all users from the database
    return jsonify([user.to_dict() for user in users])  # this is a list comprehension that returns a list of dictionaries of all users
    


# builds actual table for DB
    db.create_all()

# strats the flask app 
if __name__ == '__main__':
    app.run(debug=True)
    
    
