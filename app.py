#!/usr/bin/python

"""
Caleb Smith-Salzberg && Anish Shenoy
SoftDev1 pd7
HW07 -- Do I Know You?
2017 - 10 - 9
"""

from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

@app.route('/')
def home():
    if session.has_key('username'): #renders welcome page if a 'username' key exists
        return redirect(url_for('welcome'))
    #session['username'] is safe b/c we checked for its existance
    return render_template('login.html') #otherwise renders the login page

@app.route('/login', methods=['POST']) #uses POST method for form submission
def login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        #the only correct username is "admin" and the only correct password is "password"
        session['username'] = 'admin' #sets the 'username' key to something so that it can be recognized
        return redirect(url_for('welcome')) #tells the user they are logged in
    return render_template('login.html') #otherwise renders the login page

@app.route('/welcome') #update to check credentials
def welcome():
    return render_template('welcome.html')

@app.route('/failed')
def failed():
    return render_template('failed.html')

@app.route('/logout')
def logout():
    session.clear() #clears the session to remove the 'username' key
    return redirect(url_for('home')) #redirects user back to homepage

if __name__ == '__main__':
    app.debug = True
    app.run()
