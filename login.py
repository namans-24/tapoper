from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\admin\Desktop\tapoper\instance\login_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'naman123'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            # Redirect to the password entry page with the email included in the URL
            return redirect(url_for('password', email=email))
        else:
            flash('Email not found. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/password/<email>', methods=['GET', 'POST'])
def password(email):
    user = User.query.filter_by(email=email).first()

    if user:
        if request.method == 'POST':
            password = request.form.get('password')
            print(len(user.password))
            print(user.password)
            if user.password == password:
                print('hi')
                flash('Login successful!', 'success')
                # You can redirect to the dashboard or another page upon successful login
                return redirect(url_for('dashboard'))
            else:
                flash('Incorrect password. Please try again.', 'danger')

        return render_template('password.html', email=email)
    else:
        flash('Email not found. Please try again.', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
