#!/usr/bin/python

"""
Caleb Smith-Salzberg && Anish Shenoy
SoftDev1 pd7
HW07 -- Do I Know You?
2017 - 10 - 9
"""

from flask import Flask, render_template, redirect, url_for, request, session, flash
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

def checklogged():
    if session.has_key('username'): #renders welcome page if a 'username' key exists
        return redirect(url_for('welcome')) #tells the user they are logged in
    return render_template('login.html') #otherwise renders the login page

def auth():
    if 'username' in request.form:
        return request.form['username'] == 'admin' and request.form['password'] == 'password'
    #the only correct username is "admin" and the only correct password is "password"
    return False

def diag_print():
        print ("\n\n\n")
        print "---Diag: flask obj---"
        print (app)
        print "---Diag: request obj---"
        print request
        print "---Diag: request.headers---"
        print request.headers
        print "---Diag: request.args---"
        print request.args
        print "---Diag: request.form---"
        print request.form

@app.route('/')
def home():
    diag_print()
    return checklogged() #renders welcome page if a 'username' key exists

@app.route('/login', methods=['POST','GET']) #uses POST method for form submission
def login():
    diag_print()
    if auth():
            session['username'] = 'admin' #sets the 'username' key to something so that it can be recognized
            return redirect(url_for('welcome')) #logs the user in
    else:
            flash("Your Username/Password was incorrect!") #Flashes an error message
    return checklogged()
    #return render_template('login.html')

@app.route('/welcome') #update to check credentials
def welcome():
    diag_print()
    if session.has_key('username'): #renders welcome page if a 'username' key exists
        return render_template('welcome.html', UN = "admin")
    return checklogged()

@app.route('/logout')
def logout():
    diag_print()
    session.clear() #clears the session to remove the 'username' key
    return redirect(url_for('home')) #redirects user back to homepage

if __name__ == '__main__':
    app.debug = True
    app.run()
