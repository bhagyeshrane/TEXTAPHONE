from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('postgres://tnjvjmfnqgqyzq:94e8bb5e51feb560ed7fe2b422cbb96da8917628142445d2d17b30264b72a509@ec2-3-214-46-194.compute-1.amazonaws.com:5432/dfufe866gh6h90')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
