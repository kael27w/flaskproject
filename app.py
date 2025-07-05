# app.py

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm

# Create the Flask application instance
app = Flask(__name__)

# You MUST add a secret key for forms to work
# In the terminal, run: python3 -c 'import secrets; print(secrets.token_hex(16))'
# Then copy the output and paste it here, replacing the placeholder text.
app.config['SECRET_KEY'] = 'f9a8b9c7d6e5f4a3b2c1d0e9f8a7b6c5' # <-- REPLACE THIS WITH YOUR OWN KEY

# This is the route for your registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # Checks if form was submitted and is valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # If valid, redirect to the home page
    return render_template('register.html', title='Register', form=form)

# This is a simple home page route so the redirect has somewhere to go
@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html', title='Home')

# This block makes the file runnable
if __name__ == '__main__':
    app.run(debug=True)