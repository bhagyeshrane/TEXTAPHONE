from flask import Flask, render_template, redirect, url_for
from wtform_fields import *
from models import *
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://tnjvjmfnqgqyzq:94e8bb5e51feb560ed7fe2b422cbb96da8917628142445d2d17b30264b72a509@ec2-3-214-46-194.compute-1.amazonaws.com:5432/dfufe866gh6h90'
db =  SQLAlchemy(app)

# Configure Flask login module
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/", methods=['GET', 'POST'])
def index():
    
    reg_form = RegistrationForm()

    # Updated database if validation successful
    if reg_form.validate_on_submit():
       username = reg_form.username.data
       password = reg_form.password.data
       
       #hashing of password for better secusrity
       hashed_pwd = pbkdf2_sha256.hash(password)

       # Add user to database
       user = User(username=username, password=hashed_pwd)
       db.session.add(user)
       db.session.commit()
       return redirect(url_for('login'))
      
    return render_template("index.html", form=reg_form)

    
@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        user_object= User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    
    return render_template('login.html', form=login_form)


@app.route("/chat", methods=['GET', 'POST'])
@login_required
def chat():
    if not current_user.is_authenticated:
        return "Please login before accessing chat "
    return "Chat with me"

@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return "logout using flask_login"


if __name__ == "__main__":
    
    app.run(debug=True)