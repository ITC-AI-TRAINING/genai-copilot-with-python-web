# Flask Demo

This folder contains Flask web application examples demonstrating various Flask concepts and features. These demos are part of the GenAI Copilot with Python web development training course.

## Files and Structure

- `hello.py`: Basic Flask application showcasing routing, templates, and static files
- `login.py`: Flask app demonstrating sessions, forms, and user authentication
- `templates/`: Contains Jinja2 HTML templates
  - `hello.html`: Simple template with conditional rendering
- `static/`: Static files directory
  - `style.css`: Basic CSS stylesheet
- `.venv/`: Virtual environment (already set up)

## Prerequisites

- Python 3.11 or higher
- Flask installed (see setup below)

## Setup

1. Navigate to this folder:

   ```bash
   cd labs/flask-demo
   ```

2. Activate the virtual environment:

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. If Flask is not installed, install it:
   ```bash
   pip install flask
   ```

## Running the Applications

### Hello World App (hello.py)

Run the basic Flask application using either method:

**Option 1: Using Python command**

```bash
python hello.py
```

**Option 2: Using Flask command**

```bash
flask --app hello run --port=5001
```

Open your browser to `http://localhost:5001` or `http://127.0.0.1:5001`

This app runs on port 5001.

### Login App (login.py)

Run the login demonstration app using either method:

**Option 1: Using Python command**

```bash
python login.py
```

**Option 2: Using Flask command**

```bash
flask --app login run --port=5002
```

Open your browser to `http://localhost:5002` or `http://127.0.0.1:5002`

This app runs on port 5002.

## Flask Concepts Demonstrated

### 1. Flask Application Initialization

```python
from flask import Flask

app = Flask(__name__)
```

- Creates a Flask application instance
- `__name__` helps Flask locate templates and static files

### 2. Routing and View Functions

```python
@app.route("/")
def hello_world():
    return "<p>Hello, Flask!</p>"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'
```

- `@app.route()` decorator maps URLs to functions
- URL variables: `<username>`, `<int:post_id>`, `<path:subpath>`
- Query parameters via `request.args`
- Input sanitization with `markupsafe.escape()`

### 3. Templates with Jinja2

```python
@app.route('/hello1/<name>')
def hello_template(name=None):
    return render_template('hello.html', person=name)
```

Template (`hello.html`):

```html
{% if person %}
<h1>Hello {{ person }}!</h1>
{% else %}
<h1>Hello, World!</h1>
{% endif %}
```

- `render_template()` renders HTML templates
- Jinja2 syntax: `{{ variable }}` for output, `{% %}` for logic
- Templates stored in `templates/` folder

### 4. Static Files

```python
url_for('static', filename='style.css')
```

- Static files (CSS, JS, images) served from `static/` folder
- `url_for()` generates URLs for static files

### 5. Sessions and User State

```python
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
```

- Sessions store user data across requests
- `app.secret_key` required for session security
- Form handling with `request.form`
- `methods=['GET', 'POST']` for different HTTP methods
- `redirect()` and `url_for()` for navigation

### 6. Logging

```python
app.logger.info('Index page accessed')
```

- Flask's built-in logger for debugging and monitoring
- Different log levels: debug, info, warning, error

### 7. URL Building and Testing

```python
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login', next='/'))
```

- `url_for()` generates URLs for routes
- `test_request_context()` for testing URL generation

## How to Verify the Concepts

### Testing Routes

1. **Basic Routes**: Visit `http://localhost:5001/` - should show "Hello, Flask!"

2. **Query Parameters**: Visit `http://localhost:5001/hello?name=YourName` - should greet you by name

3. **URL Variables**:
   - `http://localhost:5001/user/john` - shows user profile
   - `http://localhost:5001/post/123` - shows post 123

4. **Templates**: Visit `http://localhost:5001/hello1/Alice` - uses template to display greeting

### Testing Sessions and Forms

1. **Login Form**: Visit `http://localhost:5002/login` - enter a username and submit

2. **Session Persistence**: After logging in, visit `http://localhost:5002/` - should show "Logged in as [username]"

3. **Logout**: Visit `http://localhost:5002/logout` - clears session

### Static Files

- The CSS file is linked but not actively used in templates; check browser dev tools to see if it's loaded

### Logging

- Check the terminal where the app is running for log messages when accessing pages

## Additional Notes

- Both apps run in debug mode (`debug=True`) for development
- The login app demonstrates basic session management (not production-ready)
- These examples show fundamental Flask concepts before building more complex applications like the JokeApp
- For production, use proper secret keys, form validation, and security measures

## Next Steps

After understanding these basics, proceed to build the main JokeApp project using the guides in the `guides/` folder.
