from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'a_very_stable_key_2026'

# Database
users_db = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Yahan simple login hai
        user = request.form.get('username')
        session['user'] = user
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form.get('username')
        if user not in users_db:
            # Naya user banaya aur code diya
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
    # Agar user login nahi hai, toh login pe bhej do
    if not user:
        return redirect(url_for('login'))
    
    # User ka code nikal
    my_code = users_db.get(user, {}).get('ref_code', 'NO_CODE')
    return render_template('my_team.html', ref_code=my_code)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)