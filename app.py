from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine

 
# Creating Flask app
app = Flask(__name__)
 
# Creating SQLAlchemy instance
db = SQLAlchemy()

user = "root"
pin = "Pendulum1597!"
host = "localhost"
db_name = "petDB"
 
# Configuring database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pin}@{host}/{db_name}"
 
# Disable modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.secret_key = 'your_secret_key_here'


class Pets(db.Model):
    __tablename__ = "petInfo"
 
    pet_name = db.Column(db.String(20), primary_key=True)
    pet_type = db.Column(db.String(5), nullable=False)
    username = db.Column(db.String(30), nullable=False)

class Users(db.Model):
    __tablename__ = "userInfo"
    user = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50))
    loggedIn = db.Column(db.Boolean, nullable=False)

# Home route
@app.route("/")
def home():
    details = Pets.query.all()
    return render_template("home.html", details=details)

 
# Add data route
@app.route("/add", methods=['GET', 'POST'])
def add_pets():
    if request.method == 'POST':
        pet_name = request.form.get('pet_name') #Title = name, author = type
        pet_type = request.form.get('pet_type')
        username = "divya"
 
        add_detail = Pets(
            pet_name=pet_name,
            pet_type=pet_type,
            username = username # foreign key constraint 
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('home'))
 
    return render_template("pets.html")


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('password')
        email = request.form.get('email')

        add_detail = Users(
            user = username,
            password = password,
            email = email,
            loggedIn = True
        )

        db.session.add(add_detail)
        db.session.commit()
        # user = Users.query.filter_by(user="divya", password=password)
        # user = Users.query.all()
        session['username'] = username
        return redirect(url_for('survey'))
    return render_template("register.html")

@app.route("/survey", methods = ['GET','POST'])
def survey():
    myUsername = session.get('username')    
    if request.method == 'POST':
        pet_name = request.form.get('petName')
        pet_type = request.form.get('petType')
        add_detail = Pets(
            pet_name = pet_name,
            pet_type = pet_type,
            username = myUsername
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("survey.html")


@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():
    myUsername = session.get('username') 
    user_pet = Pets.query.filter_by(username = myUsername).first()   
    return render_template("dashboard.html", myPet = user_pet)

if __name__ == "__main__":
    #create_db()
    app.run(debug=True)


