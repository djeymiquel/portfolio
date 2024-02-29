from flask import Flask, render_template,request,url_for,redirect

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def base():
    title = "Djey Miquel"
    return render_template('homepage.html', title=title)
    #return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    title = "Home"
    return render_template('homepage.html', title=title)
    
@app.route('/about', methods=['GET'])
def about():
    title = "About"
    return render_template('about.html', title=title)

@app.route('/contact', methods=['GET'])
def contact():
    title = "Contact"
    return render_template('contact.html', title=title)

@app.route('/portfolio', methods=['GET'])
def portfolio():
    title = "Portfolio"
    return render_template('portfolio.html', title=title)

@app.route('/skills', methods=['GET'])
def skills():
    title = "Skills"
    return render_template('skills.html', title=title)

@app.route('/certificates', methods=['GET'])
def certificates():
    title = "Certificates"
    return render_template('certificates.html', title=title)

