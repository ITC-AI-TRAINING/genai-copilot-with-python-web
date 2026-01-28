# Flask JokeApp v2

A Flask web application that fetches and displays jokes from the [JokeAPI](https://v2.jokeapi.dev). This app demonstrates building a simple web application with Flask, integrating external APIs, and handling errors gracefully.

## Features

- **Home Page**: Welcome page with navigation
- **Random Jokes**: Fetch jokes from any category
- **Category-specific Jokes**: Get jokes from specific categories (Programming, Miscellaneous, Dark, etc.)
- **About & Contact Pages**: Static information pages
- **Error Handling**: Graceful handling of API failures and network issues
- **Responsive Design**: Bootstrap-based UI for mobile-friendly experience

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Setup Instructions

### 1. Clone or Download the Project

Navigate to the project directory:

```bash
cd flask-jokeapp-v2
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install flask requests
```

### 5. Run the Application

**Option 1: Using Flask CLI (recommended)**

**On macOS/Linux:**

```bash
flask run
```

**On Windows:**

```bash
flask run
```

**Option 2: Direct Python execution**

```bash
python app.py
```

The application will start on `http://localhost:5000` (or `http://0.0.0.0:5000`).

## Usage

### Web Interface

1. Open your browser and go to `http://localhost:5000`
2. Navigate through the pages using the menu:
   - **Home**: Welcome page
   - **About**: Information about the app
   - **Contact**: Contact information
   - **Get a Joke**: Random joke from any category
   - **Joke by Category**: Jokes filtered by category

### API Endpoints

- `GET /` - Home page
- `GET /about` - About page
- `GET /contact` - Contact page
- `GET /joke` - Random joke
- `GET /joke/<category>` - Joke from specific category (e.g., `/joke/Programming`)
- `GET /health` - Health check endpoint (returns JSON status)

### Supported Categories

- Any (default)
- Programming
- Miscellaneous
- Dark
- Pun
- Spooky
- Christmas

## Testing

### API Testing Script

Run the included test script to verify API connectivity:

```bash
python test_api.py
```

This will fetch a sample joke and display the API response structure.

### Running Unit Tests (if available)

If pytest is installed and test files exist:

```bash
pip install pytest
pytest
```

## Project Structure

```
flask-jokeapp-v2/
├── app.py                 # Main Flask application
├── test_api.py           # API testing script
├── venv/                 # Virtual environment (created during setup)
├── static/
│   └── style.css         # Custom CSS styles
└── templates/
    ├── base.html         # Base template with Bootstrap
    ├── home.html         # Home page template
    ├── about.html        # About page template
    ├── contact.html      # Contact page template
    ├── joke.html         # Joke display template
    └── error.html        # Error page template
```

## Dependencies

- **Flask**: Web framework for Python
- **requests**: HTTP library for API calls

## Configuration

The application runs with the following default settings:

- Host: 0.0.0.0 (accessible from any network interface)
- Port: 5000
- Debug mode: Enabled (auto-reloads on code changes)

## Error Handling

The app includes comprehensive error handling for:

- Network timeouts (5-second timeout on API calls)
- Connection failures
- HTTP errors
- Invalid JSON responses
- API-specific errors

## Development

To modify the application:

1. Edit `app.py` for routes and logic
2. Modify templates in the `templates/` folder
3. Update styles in `static/style.css`
4. Test changes by running the app and visiting the endpoints

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` or kill the process using port 5000
2. **Import errors**: Ensure virtual environment is activated and dependencies are installed
3. **Template not found**: Check that template files exist in the `templates/` folder
4. **API failures**: Check internet connection and JokeAPI status

### Debug Mode

With debug mode enabled, Flask will:

- Auto-reload on code changes
- Show detailed error pages
- Provide interactive debugger

## Contributing

This is a training project for learning Flask and GitHub Copilot. Feel free to experiment and modify the code.

## License

This project is for educational purposes.
