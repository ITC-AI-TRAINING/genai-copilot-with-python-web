from flask import Flask, render_template, jsonify
from datetime import datetime
import requests

app = Flask(__name__)
app_version = "1.0.0"


@app.context_processor
def inject_year():
    """Inject current year into all templates."""
    return {'current_year': datetime.now().year}


def get_joke(category="Any"):
    """
    Fetch a joke from JokeAPI.
    
    Args:
        category (str): Joke category (Any, Programming, Miscellaneous, Dark, etc.)
                       Defaults to "Any" for random category selection.
    
    Returns:
        dict: A dictionary containing:
            - 'success' (bool): True if joke fetched successfully, False otherwise
            - 'joke_type' (str): Either 'single' or 'twopart'
            - 'joke' (str): The complete joke text (for single jokes)
            - 'setup' (str): Setup text (for two-part jokes)
            - 'delivery' (str): Punchline text (for two-part jokes)
            - 'category' (str): The joke category
            - 'error' (str): Error message if request fails, empty string if successful
    
    Example:
        >>> result = get_joke("Programming")
        >>> if result['success']:
        ...     if result['joke_type'] == 'single':
        ...         print(result['joke'])
        ...     else:
        ...         print(f"{result['setup']}\\n{result['delivery']}")
        ... else:
        ...     print(f"Error: {result['error']}")
    """
    try:
        # Construct API endpoint
        api_url = f"https://v2.jokeapi.dev/joke/{category}"
        
        # Make request with 5 second timeout
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if API returned an error
        if data.get('error'):
            return {
                'success': False,
                'joke_type': None,
                'joke': None,
                'setup': None,
                'delivery': None,
                'category': None,
                'error': f"JokeAPI error: {data.get('message', 'Unknown error')}"
            }
        
        # Extract joke data based on type
        joke_type = data.get('type', 'single')
        
        if joke_type == 'single':
            return {
                'success': True,
                'joke_type': 'single',
                'joke': data.get('joke', ''),
                'setup': None,
                'delivery': None,
                'category': data.get('category', ''),
                'error': ''
            }
        else:  # twopart
            return {
                'success': True,
                'joke_type': 'twopart',
                'joke': None,
                'setup': data.get('setup', ''),
                'delivery': data.get('delivery', ''),
                'category': data.get('category', ''),
                'error': ''
            }
    
    except requests.exceptions.Timeout:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': 'Request timed out. The API is taking too long to respond.'
        }
    
    except requests.exceptions.ConnectionError:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': 'Connection failed. Please check your internet connection and try again.'
        }
    
    except requests.exceptions.HTTPError as e:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': f'HTTP Error {e.response.status_code}: {e.response.reason}'
        }
    
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': f'Request error: {str(e)}'
        }
    
    except ValueError:  # JSON decode error
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': 'Failed to parse API response. Invalid JSON received.'
        }
    
    except Exception as e:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': f'Unexpected error: {str(e)}'
        }


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
