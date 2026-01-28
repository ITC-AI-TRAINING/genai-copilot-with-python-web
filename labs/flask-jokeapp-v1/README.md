# JokeApp v1

This is the first version of JokeApp, a Flask web application designed to demonstrate basic Flask concepts and prepare for integrating the JokeAPI. This version includes static pages with Bootstrap styling but does not yet fetch jokes from the API.

## Project Structure

```
flask-jokeapp-v1/
├── app.py                 # Main Flask application
├── static/
│   └── style.css          # Custom CSS styles
└── templates/
    ├── base.html          # Base template with Bootstrap navbar and footer
    ├── home.html          # Home page with hero section and feature cards
    ├── about.html         # About page with app description
    └── contact.html       # Contact page
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup

1. **Navigate to the project directory:**

   ```bash
   cd labs/flask-jokeapp-v1
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Flask:**
   ```bash
   pip install flask
   ```

## Configuration

No additional configuration is required for this basic version. The app runs with default Flask settings:

- Debug mode enabled for development
- Host: 0.0.0.0 (accessible from any network interface)
- Port: 5000

## Running the Application

1. **Start the Flask development server:**

   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**

   ```
   http://localhost:5000
   ```

3. **Test the routes:**
   - Home: `http://localhost:5000/`
   - About: `http://localhost:5000/about`
   - Contact: `http://localhost:5000/contact`
   - Health check: `http://localhost:5000/health` (returns JSON)
   - Greet: `http://localhost:5000/greet/YourName` (personalized greeting)

## Features

### Current Features (v1.0.0)

- **Responsive Web Design**: Built with Bootstrap 5 for mobile-first, responsive layout
- **Navigation**: Clean navbar with links to Home, About, and Contact pages
- **Templating**: Uses Jinja2 templates with inheritance (base.html)
- **Static Files**: Custom CSS for enhanced styling
- **Context Processor**: Automatically injects current year into all templates
- **Health Endpoint**: JSON API endpoint for application health checks
- **Dynamic Greetings**: URL-based personalized greetings

### Templates and Styling

- **Base Template**: Includes Bootstrap CDN, custom CSS, navbar, and footer with copyright
- **Home Page**: Hero section with welcome message and feature overview cards
- **About Page**: Information about the app, technology stack, and features
- **Contact Page**: Placeholder contact information
- **Custom CSS**: Variables for consistent theming, typography, and component styling

## Flask Concepts Demonstrated

- **Application Factory**: Basic Flask app initialization
- **Routing**: Multiple routes with and without parameters
- **Template Rendering**: `render_template()` with context variables
- **Static File Serving**: CSS files served via `url_for('static', filename='...')`
- **Context Processors**: Global variables available in all templates
- **JSON Responses**: `jsonify()` for API-like endpoints
- **URL Building**: `url_for()` for internal links

## Development Notes

- This is a foundational version before API integration
- Built with GitHub Copilot assistance for code generation
- Follows Flask best practices for structure and organization
- Ready for extension to add JokeAPI integration in future versions

## Next Steps

To continue development:

1. Add JokeAPI integration (see course guides)
2. Implement joke fetching and display
3. Add category filtering
4. Include user forms for custom joke requests
5. Add testing with pytest

## Troubleshooting

- **Port already in use**: Change the port in `app.py` or kill the process using `lsof -ti:5000 | xargs kill -9`
- **Template not found**: Ensure you're running from the correct directory with `templates/` folder
- **Import errors**: Make sure Flask is installed in the virtual environment

## License

This is a training project for educational purposes.
