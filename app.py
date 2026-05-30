from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rpay_secret_2026'

# --- ROUTES ---

@app.route('/')
def index(): 
    return redirect(url_for('login'))

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

@app.route('/dashboard')
def dashboard(): 
    return render_template('dashboard.html')

@app.route('/deposit')
def deposit(): 
    return render_template('deposit.html')

@app.route('/confirm_order/<amount>')
def confirm_order(amount): 
    return render_template('confirm_order.html', amount=amount)

@app.route('/bank')
def bank(): 
    return render_template('bank.html')

@app.route('/add_bank')
def add_bank(): 
    return render_template('add_bank.html')

@app.route('/profile')
def profile(): 
    user_data = {'id': '1', 'balance': '1,00,000', 'quota': '5000'}
    return render_template('profile.html', user=user_data)

@app.route('/recharge_history')
def recharge_history(): 
    return render_template('recharge_history.html')

@app.route('/token_history')
def token_history(): 
    return render_template('token_history.html')

@app.route('/contact')
def contact(): 
    return render_template('contact.html')

# --- FIX KIYA GAYA ROUTE ---
@app.route('/my_team')
def my_team(): 
    # Yahan data define kar diya hai taaki error na aaye
    user_data = {'referral_code': 'RPAY123'}
    team_list = [] # Agar team khali hai, toh empty list
    return render_template('my_team.html', 
                           user=user_data, 
                           team=team_list, 
                           team_count=0, 
                           team_value=0, 
                           today_earning=0)

@app.route('/logout')
def logout(): 
    session.clear() 
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)