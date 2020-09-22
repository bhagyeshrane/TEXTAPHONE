from flask import Flask, render_template, redirect, url_for

from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://tnjvjmfnqgqyzq:94e8bb5e51feb560ed7fe2b422cbb96da8917628142445d2d17b30264b72a509@ec2-3-214-46-194.compute-1.amazonaws.com:5432/dfufe866gh6h90'
db =  SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    
    reg_form = RegistrationForm()

    # Updated database if validation successful
    if reg_form.validate_on_submit():
       username = reg_form.username.data
       password = reg_form.password.data
       # Add user to database
       user = User(username=username, password=password)
       db.session.add(user)
       db.session.commit()
       return redirect(url_for('login'))
      
    return render_template("index.html", form=reg_form)

    
@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        return "logged in!"
    
    return render_template(login.html)


if __name__ == "__main__":
    
    app.run(debug=True)