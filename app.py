from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'final_stable_key_2026'

orders_db = [
    {'id': 1, 'amount': 200, 'seller': 'Amit', 'bank': 'SBI', 'acc': '1234567890', 'ifsc': 'SBIN0001'},
    {'id': 2, 'amount': 8000, 'seller': 'Rahul', 'bank': 'HDFC', 'acc': '0987654321', 'ifsc': 'HDFC0002'}
]

# Auth Routes
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# Game & Profile Routes
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html', orders=orders_db)

@app.route('/payment_confirm/<int:order_id>')
def payment_confirm(order_id):
    order = next((o for o in orders_db if o['id'] == order_id), None)
    return render_template('payment_confirm.html', order=order)

@app.route('/bank_account', methods=['GET', 'POST'])
def bank_account():
    return render_template('bank_account.html', bank_accounts=[])

# --- FIXED PROFILE ROUTES ---
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/recharge_history')
def recharge_history():
    return render_template('recharge_history.html')

@app.route('/token_history')
def token_history():
    return render_template('token_history.html')

@app.route('/edit_profile')
def edit_profile():
    return render_template('edit_profile.html')

@app.route('/my_team')
def my_team():
    return render_template('my_team.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)