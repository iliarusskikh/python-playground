from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-temporary-dev-key-123pyt'  # Needed for flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

# Create database and tables within app context
with app.app_context():
    db.create_all()

# Route for home page (list all users)
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# Route to add a new user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        if name and age:
            try:
                new_user = User(name=name, age=int(age))
                db.session.add(new_user)
                db.session.commit()
                flash('User added successfully!', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error adding user: {e}', 'error')
        else:
            flash('Name and age are required!', 'error')
    return render_template('add_user.html')

# Route to edit an existing user
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.age = int(request.form['age']) if request.form['age'] else None
        try:
            db.session.commit()
            flash('User updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating user: {e}', 'error')
    return render_template('edit_user.html', user=user)

# Route to delete a user
@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting user: {e}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)