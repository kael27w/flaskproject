# app.py

from flask import Flask, render_template, url_for, flash, redirect, request
import git
from forms import RegistrationForm

# Create the Flask application instance
app = Flask(__name__)

# Your Secret Key
app.config['SECRET_KEY'] = 'f9a8b9c7d6e5f4a3b2c1d0e9f8a7b6c5' # <-- REMEMBER TO USE YOUR OWN KEY

# This is the new route that listens for the GitHub webhook
@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/kael27w/flaskproject')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

# This is the route for your registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# This is the home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html', title='Home')

# This block makes the file runnable for local testing
if __name__ == '__main__':
    app.run(debug=True)