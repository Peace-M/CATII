from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



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