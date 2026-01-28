from flask import Flask, jsonify, render_template

app = Flask(__name__)

app_version = "1.0.0"

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html', app_version=app_version, welcome_message="Welcome to JokeApp!")

@app.route('/health')
def health():
    """Returns the health status of the application in JSON format."""
    return jsonify({"status": "ok"})

@app.route('/greet/<name>')
def greet(name):
    """Returns a personalized greeting."""
    return f"Hello, {name}!"

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')

@app.context_processor
def inject_year():
    from datetime import datetime
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)