from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'
            ]='postgresql://user_1:user123@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, heght_):
        self.email_ = email_
        self.height_ = heght_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == "POST":
        email = request.form['email']
        height = request.form['height']
       
        if(db.session.query(Data).filter(Data.email_ == email).count() >= 1):
            return render_template("index.html",text="Seems like email you enter is duplicate. please try again")
        data=Data(email,height)
        db.session.add(data)
        avg_height = db.session.query(func.avg(Data.height_)).scalar()
        avg_height = round(avg_height,1)
        count=db.session.query(Data.height_).count()
        send_email(email,height,avg_height,count)
        db.session.commit()
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()