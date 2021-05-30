from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///root.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(400), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __user__(self,firstname,lastname,email,message,date_added):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message
        self.date_added = date_added
        
        


@app.route('/', methods = ['GET','POST'])
def add_user ():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        message = request.form['message']
        new_entry = User(firstname, lastname, email, message )

        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/contact')
        except:
            return "Error Submitting"
    else:
        return render_template('index.html')
          


    

     



@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/portfolio-page.html')
def portfolio():
    return render_template('portfolio-page.html')  

@app.route('/portfolioII-page.html')
def portfolioll():
    return render_template('portfolioII-page.html')



if __name__   == "__main__":
    app.run(debug=True)  