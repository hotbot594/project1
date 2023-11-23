from flask import flash, redirect, render_template, request, jsonify, make_response
import json
from app import *
from controllers import *


app.route('/')
def main():
    return render_template('main.html')

@app.route('/roll', methods=['GET', 'POST'])
def roll():
    if request.method == 'POST':
        bytes_data = request.data
        data = json.loads(bytes_data.decode())
        print(data)
    return render_template('roll.html')



@app.route('/register', methods=["GET", 'POST'])
def reg():
    if request.method != 'POST':
        return render_template('reg.html')
    is_password_match=request.form.get('password')==request.form.get('confirm_pass')
    print(request.form.get('password'))
    print(request.form.get('confirm_pass'))
    if is_password_match:
        register_user(request.form)
        return redirect('/login')
    else:
        flash('password don\'t match')
        return redirect('/reg')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method != 'POST':
        return render_template('login.html')
    
    try:
        user_id = int(request.form.get('name').split('_')[1])
    except:
        flash('Enter your username in format "username_1"')
        return redirect('/login')

    password = request.form.get('password')

    user = get_object_by_id(user_id, User)
    is_password_correct = check_password_hash(user.password, password)

    if not user or not is_password_correct:
        flash('Either there\'s no user with this username or you entered incorrect password')
        return redirect('/login')

    login_user(user)
    
    return redirect('/')


