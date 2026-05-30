from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(_name_)
app.secret_key = 'final_stable_key_2026'

# Dummy Database
users_db = {} # Format: {'username': {'password': '...', 'ref_code': '...'}}
orders_db = [
    {'id': 1, 'amount': 200, 'seller': 'Amit', 'bank': 'SBI', 'acc': '1234567890', 'ifsc': 'SBIN0001'},
    {'id': 2, 'amount': 8000, 'seller': 'Rahul', 'bank': 'HDFC', 'acc': '0987654321', 'ifsc': 'HDFC0002'}
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session['user'] = user
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        # Har user ke liye naya code
        code = str(uuid.uuid4())[:8]
        users_db[user] = {'ref_code': code}
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/my_team')
def my_team():
    user = session.get('user')
    # Agar user login hai, toh uska code nikal lo
    my_code = users_db.get(user, {}).get('ref_code', 'NO_CODE')
    return render_template('my_team.html', ref_code=my_code)

# Baki routes same rahenge...
@app.route('/deposit')
def deposit(): return render_template('deposit.html', orders=orders_db)

@app.route('/profile')
def profile(): return render_template('profile.html')

if _name_ == '_main_':
    app.run(debug=True)