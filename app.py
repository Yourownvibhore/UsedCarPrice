from flask import Flask, render_template, request
import os
import sys

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__=="__main__":
    app.run(debug=True)