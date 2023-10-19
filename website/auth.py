from flask import Blueprint

authentication = Blueprint('authentication', __name__)

@authentication.route('/login')
def login():
    return "<p>login</p>"

@authentication.route('/logout')
def logout():    
    return "<p>logout</p>"

@authentication.route('/sign-up')
def signup():
    return "<p>Sign Up</p>"