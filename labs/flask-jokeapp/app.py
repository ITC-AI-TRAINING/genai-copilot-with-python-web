from flask import Flask, render_template, jsonify
from datetime import datetime
from services.joke_service import get_joke, ALLOWED_CATEGORIES

app = Flask(__name__)
app_version = "1.0.0"


@app.context_processor
def inject_year():
    """Inject current year into all templates."""
    return {'current_year': datetime.now().year}


@app.route('/')
def home():
    """Render the home page."""
    welcome_message = "Get a laugh with our collection of jokes!"
    return render_template('home.html', app_version=app_version, welcome_message=welcome_message)


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/joke')
def get_random_joke():
    """
    Fetch and display a random joke from any category.
    
    Returns:
        Rendered template with joke data or error message.
    """
    joke_data = get_joke("Any")
    return render_template('joke.html', joke_data=joke_data)


@app.route('/joke/<category>')
def get_joke_by_category(category):
    """
    Fetch and display a joke from a specified category.
    
    Args:
        category (str): The joke category (Programming, Miscellaneous, Dark, etc.)
    
    Returns:
        Rendered template with joke data or error message.
    """
    # Sanitize category name (capitalize first letter)
    category = category.capitalize()
    
    joke_data = get_joke(category)
    return render_template('joke.html', joke_data=joke_data, category=category)


@app.route('/health')
def health():
    """Return the health status of the application."""
    return jsonify(status='ok')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
