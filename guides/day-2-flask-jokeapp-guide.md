# Day 2: API Integration, Testing & Best Practices

**Duration:** 4.5 Hours  
**Modules Covered:**

- Module 3: Consuming JokeAPI in Flask (2 hrs)
- Module 4: Enhancing Flask App with Copilot (1.5 hrs)
- Module 5: Wrap-up & Best Practices (1 hr)

---

## 🎯 Learning Objectives

By the end of Day 2, you will be able to:

- ✅ Integrate external REST APIs (JokeAPI) into Flask
- ✅ Handle API requests and parse JSON responses
- ✅ Implement comprehensive error handling
- ✅ Create forms for user input with validation
- ✅ Refactor code into service layers
- ✅ Write unit tests with pytest
- ✅ Add logging and documentation
- ✅ Configure Flask for production
- ✅ Deploy a complete, functional JokeApp

---

## 📋 Day 1 Quick Recap (5 minutes)

Yesterday you built:

- ✅ Flask app structure with routes
- ✅ Templates with Jinja2 and Bootstrap
- ✅ Multi-page navigation
- ✅ Custom styling

Today: **Make it functional with real jokes!** 🎭

---

## Module 3: Consuming JokeAPI in Flask (2 hours)

### Step 3.1: Understanding JokeAPI (15 minutes)

#### 3.1.1 Explore JokeAPI Documentation

**Visit:** https://v2.jokeapi.dev/

**Key Endpoints:**

- `GET https://v2.jokeapi.dev/joke/Any` - Random joke
- `GET https://v2.jokeapi.dev/joke/Programming` - Category-specific
- `GET https://v2.jokeapi.dev/joke/Programming,Misc` - Multiple categories

**Joke Types:**

1. **Single:** One-liner jokes (`joke` field)
2. **Two-part:** Setup and delivery (`setup` and `delivery` fields)

**Test in Browser:** Open https://v2.jokeapi.dev/joke/Programming and observe the JSON response.

#### 3.1.2 Understand JSON Response Structure

Use Copilot Chat:

```
Explain the JSON response structure from JokeAPI.
Show examples of both single and two-part joke formats.
What fields are always present vs optional?
```

**✓ Checkpoint:** You understand the difference between single and two-part jokes.

---

### Step 3.2: Install and Use Requests Library (20 minutes)

#### 3.2.1 Install Requests

```bash
pip install requests
```

#### 3.2.2 Test API Call in Python Console

Create a test file `test_api.py`:

**Prompt Copilot Chat:**

```
Create a simple Python script test_api.py that:
- Imports requests
- Fetches a joke from https://v2.jokeapi.dev/joke/Programming
- Prints the JSON response in a readable format
- Includes error handling for network issues
```

**Run it:**

```bash
python test_api.py
```

**✓ Checkpoint:** Successfully fetched and displayed a joke from the API.

---

### Step 3.3: Create JokeAPI Helper Function (30 minutes)

#### 3.3.1 Generate get_joke() Function

Use Copilot Chat with this comprehensive prompt:

```
In app.py, create a function get_joke() that:
- Takes an optional category parameter (default: "Any")
- Uses the requests library to fetch from https://v2.jokeapi.dev/joke/{category}
- Returns a dictionary with:
  - 'success': True/False
  - 'joke_type': 'single' or 'twopart'
  - 'joke': the joke text (for single jokes)
  - 'setup' and 'delivery': for two-part jokes
  - 'category': the joke category
  - 'error': error message if request fails
- Includes try/except for network errors
- Has proper docstrings with parameter and return type documentation
- Handles timeout (5 seconds)
- Returns user-friendly error messages
```

#### 3.3.2 Review and Understand the Generated Code

**Key concepts to verify:**

- `requests.get()` with timeout parameter
- `response.json()` to parse JSON
- `response.raise_for_status()` for HTTP errors
- Try-except blocks for `requests.exceptions.RequestException`

#### 3.3.3 Test the Function

Add a test call at the bottom of `app.py` (temporary):

```python
if __name__ == '__main__':
    # Test the function
    result = get_joke('Programming')
    print(result)

    app.run(debug=True)
```

**✓ Checkpoint:** Function successfully returns joke data or error messages.

---

### Step 3.4: Create Joke Display Routes (30 minutes)

#### 3.4.1 Add Joke Routes to app.py

Use Copilot Chat:

```
Add two routes to app.py:
1. /joke - fetches a random joke (Any category) and renders joke.html
2. /joke/<category> - fetches a joke from specified category and renders joke.html
Both routes should:
- Call get_joke() with appropriate parameters
- Pass the joke data to the template
- Handle errors gracefully
- Include docstrings
```

#### 3.4.2 Create joke.html Template

Use Copilot Chat:

```
Create templates/joke.html that extends base.html and:
- Displays the joke category as a badge
- For single jokes: displays the joke in a Bootstrap card
- For two-part jokes: shows setup and delivery separately with labels
- Uses different styling for setup (bold) and delivery (regular)
- Displays error messages in a Bootstrap alert-danger if present
- Has a "Get Another Joke" button that links to /joke
- Has a "Back to Home" button
- Uses Bootstrap card component with shadow
- Includes emoji based on category (💻 for Programming, 🎭 for Misc, etc.)
```

**✓ Checkpoint:** Visiting http://127.0.0.1:5000/joke displays a random joke.

---

### Step 3.5: Add Category Selection to Home Page (25 minutes)

#### 3.5.1 Create Category Dropdown Form

Use Copilot Chat:

```
Update templates/home.html to add a Bootstrap form with:
- A heading "Choose Your Joke Category"
- A select dropdown with options: Any, Programming, Misc, Dark, Pun, Spooky, Christmas
- Each option should have appropriate emoji
- A submit button "Get Joke" with primary styling
- Form uses GET method and submits to /joke/<category>
- Use JavaScript or form action to dynamically build the URL based on selection
- Add nice spacing and centering
```

#### 3.5.2 Add JavaScript for Dynamic Form Submission

Use Copilot Chat if needed:

```
Add JavaScript to home.html that:
- Listens for form submit
- Gets selected category value
- Redirects to /joke/<category>
- Or use a simpler approach with a button that changes href based on selection
```

**✓ Checkpoint:** Selecting a category and clicking "Get Joke" shows a joke from that category.

---

### Step 3.6: Implement Comprehensive Error Handling (20 minutes)

#### 3.6.1 Handle Invalid Categories

Use Copilot Chat:

```
Update app.py:
- Create a list ALLOWED_CATEGORIES with valid JokeAPI categories
- In the /joke/<category> route, validate the category
- If invalid, render an error page or redirect to home with a flash message
- Add appropriate HTTP status codes (404 for not found, 400 for bad request)
```

#### 3.6.2 Create Error Template

Use Copilot Chat:

```
Create templates/error.html that:
- Extends base.html
- Displays an error message passed from the route
- Has a Bootstrap alert-warning
- Includes a "Go Home" button
- Shows a friendly error emoji 😕
```

#### 3.6.3 Test Error Scenarios

Test these URLs:

1. http://127.0.0.1:5000/joke/InvalidCategory (should show error)
2. Temporarily break the API URL in get_joke() (should show network error)
3. Test with internet disconnected

**✓ Checkpoint:** All error scenarios display user-friendly messages.

---

## ☕ Break (15 minutes)

---

## Module 4: Enhancing Flask App with Copilot (1.5 hours)

### Step 4.1: Refactor to Service Layer (25 minutes)

#### 4.1.1 Create Service Module

Use Copilot Chat:

```
Refactor the JokeAPI code:
1. Create a new folder: services/
2. Create services/__init__.py (empty)
3. Create services/joke_service.py
4. Move get_joke() function to joke_service.py
5. Add a helper function build_joke_url(category, joke_type=None) that constructs the API URL
6. Add constants for API_BASE_URL and ALLOWED_CATEGORIES
7. Update app.py to import from services.joke_service
8. Keep all error handling, docstrings, and type hints
```

#### 4.1.2 Update app.py Imports

Verify imports in `app.py`:

```python
from services.joke_service import get_joke, ALLOWED_CATEGORIES
```

#### 4.1.3 Benefits of Service Layer

**Prompt Copilot Chat:**

```
Explain the benefits of separating API logic into a service layer.
What are the advantages for testing, maintenance, and scalability?
```

**✓ Checkpoint:** App works exactly as before, but code is better organized.

---

### Step 4.2: Add Custom Joke Form (25 minutes)

#### 4.2.1 Create Advanced Joke Request Form

Use Copilot Chat:

```
Update templates/home.html to add a second form section:
- Heading "Custom Joke Request"
- Select for joke type: Any, Single, Twopart
- Select for category: Any, Programming, Misc, Dark, Pun
- Multi-select for multiple categories (optional)
- Checkboxes for flags to exclude: nsfw, religious, political, racist, sexist
- Submit button "Get Custom Joke"
- Form should POST to /custom-joke
- Use Bootstrap form styling with proper spacing
```

#### 4.2.2 Create Custom Joke Route

Use Copilot Chat:

```
Add a route /custom-joke in app.py that:
- Accepts POST method
- Reads form data (category, joke_type, flags)
- Builds appropriate JokeAPI URL with parameters
- Calls a new function get_custom_joke() in joke_service.py
- Renders joke.html with the result
- Includes validation and error handling
```

#### 4.2.3 Update Service for Custom Requests

Use Copilot Chat:

```
Add function get_custom_joke() to services/joke_service.py that:
- Accepts category, joke_type, and flags_to_exclude
- Constructs URL with query parameters
- Example: /joke/Programming?type=single&blacklistFlags=nsfw,religious
- Returns joke data in same format as get_joke()
```

**✓ Checkpoint:** Custom form allows filtering jokes by type and flags.

---

### Step 4.3: Add Input Validation and Sanitization (20 minutes)

#### 4.3.1 Implement Form Validation

Use Copilot Chat:

```
Create utils/validators.py with functions:
- validate_category(category): checks against ALLOWED_CATEGORIES
- validate_joke_type(joke_type): checks against ['any', 'single', 'twopart']
- sanitize_input(user_input): removes potentially harmful characters
- All functions should return (is_valid, error_message) tuple
- Include docstrings
```

#### 4.3.2 Apply Validation in Routes

Use Copilot Chat:

```
Update app.py routes to use validators:
- Import validation functions
- Validate all user inputs before processing
- Return 400 Bad Request with error message for invalid inputs
- Log validation failures
```

#### 4.3.3 Add Flash Messages

Use Copilot Chat:

```
Add Flask flash messages to app.py:
- Flash success message when joke is fetched
- Flash error message for validation failures
- Update base.html to display flash messages with Bootstrap alerts
- Include dismiss button for alerts
```

**✓ Checkpoint:** Invalid inputs show friendly error messages, valid inputs work correctly.

---

### Step 4.4: Testing with pytest (40 minutes)

#### 4.4.1 Install Testing Dependencies

```bash
pip install pytest pytest-mock
```

#### 4.4.2 Create Test Structure

```bash
mkdir tests
touch tests/__init__.py
```

#### 4.4.3 Generate Service Tests

Use Copilot Chat:

```
Create tests/test_joke_service.py with pytest tests that:
1. Test get_joke() with no parameters returns a joke
2. Test get_joke('Programming') returns Programming joke
3. Test get_joke('InvalidCategory') returns error
4. Mock requests.get to return a sample joke response
5. Mock requests.get to raise RequestException and verify error handling
6. Test build_joke_url() generates correct URLs
7. Use pytest fixtures for mock responses
8. Include docstrings and assertions
9. Use @pytest.mark.parametrize for testing multiple categories
```

#### 4.4.4 Generate Route Tests

Use Copilot Chat:

```
Create tests/test_routes.py with Flask test client tests:
1. Create fixture for Flask test client
2. Test GET / returns 200 and contains "JokeApp"
3. Test GET /about returns 200
4. Test GET /joke returns 200 and contains joke data
5. Test GET /joke/Programming returns 200
6. Test GET /joke/InvalidCategory returns 400 or 404
7. Test POST /custom-joke with valid data returns 200
8. Test POST /custom-joke with invalid data returns 400
9. Mock get_joke() to avoid real API calls in tests
10. Use assertions to check response status codes and content
```

#### 4.4.5 Run Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pip install pytest-cov
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_joke_service.py -v
```

**✓ Checkpoint:** All tests pass successfully.

---

## ☕ Break (10 minutes)

---

## Module 5: Wrap-up & Best Practices (1 hour)

### Step 5.1: Add Logging (15 minutes)

#### 5.1.1 Configure Logging

Use Copilot Chat:

```
Add logging configuration to app.py:
1. Import Python logging module
2. Configure logging with:
   - Level: INFO for production, DEBUG for development
   - Format: timestamp, level, message
   - File handler: logs/flask_app.log
   - Console handler for development
3. Add log messages:
   - When jokes are fetched successfully
   - When API calls fail
   - When invalid categories are requested
   - When the app starts
4. Create logs/ directory if it doesn't exist
```

#### 5.1.2 Test Logging

```bash
# Create logs directory
mkdir -p logs

# Run app and check logs
python app.py

# View logs
cat logs/flask_app.log
```

**✓ Checkpoint:** Logs directory contains log file with timestamped entries.

---

### Step 5.2: Add Comprehensive Documentation (15 minutes)

#### 5.2.1 Generate Docstrings

Use Copilot Chat:

```
Review all Python files and add or improve docstrings:
- Use Google style or NumPy style
- Include for all modules, classes, functions
- Document parameters with types
- Document return values
- Document exceptions that can be raised
- Add usage examples for complex functions
Files: app.py, services/joke_service.py, utils/validators.py, all test files
```

#### 5.2.2 Create Project README

Use Copilot Chat:

```
Create README.md with:
- Project title and description
- Features list with emoji
- Screenshots section (placeholder text)
- Prerequisites
- Setup instructions (virtual environment, installation, running)
- How to run tests
- Project structure tree
- Configuration options
- API documentation (routes and their purposes)
- Credits to JokeAPI
- License information (MIT)
- Contributing guidelines
- Use proper Markdown formatting
```

**✓ Checkpoint:** README.md provides complete project documentation.

---

### Step 5.3: Configuration Management (15 minutes)

#### 5.3.1 Create Configuration Classes

Use Copilot Chat:

```
Create config.py with:
1. BaseConfig class with common settings:
   - SECRET_KEY (from environment or default)
   - JOKEAPI_BASE_URL
   - ALLOWED_CATEGORIES
2. DevelopmentConfig(BaseConfig):
   - DEBUG = True
   - TESTING = False
3. ProductionConfig(BaseConfig):
   - DEBUG = False
   - Add security headers
4. TestingConfig(BaseConfig):
   - TESTING = True
   - Different database if applicable
5. Config dictionary to select based on environment
```

#### 5.3.2 Update app.py to Use Config

Use Copilot Chat:

```
Update app.py to:
- Import config classes
- Load configuration based on environment variable FLASK_ENV
- Default to DevelopmentConfig
- Use app.config.from_object(config)
```

#### 5.3.3 Create Environment File Template

Use Copilot Chat:

```
Create .env.example with:
- SECRET_KEY=your-secret-key-here
- FLASK_ENV=development
- JOKEAPI_BASE_URL=https://v2.jokeapi.dev
- Comments explaining each variable
Also create .gitignore with: venv/, .env, __pycache__/, *.pyc, logs/, .pytest_cache/, htmlcov/
```

**Install and use python-dotenv:**

```bash
pip install python-dotenv
```

Use Copilot to update app.py:

```
Add python-dotenv to app.py to load environment variables from .env file
```

**✓ Checkpoint:** App uses configuration from environment variables.

---

### Step 5.4: Security and Production Readiness (15 minutes)

#### 5.4.1 Security Best Practices

Use Copilot Chat:

```
Review the Flask app for security issues and add:
1. Input sanitization for all user inputs
2. CSRF protection (show how to use Flask-WTF)
3. Secure headers (use Flask-Talisman or manual headers)
4. Rate limiting to prevent API abuse
5. Validate and sanitize all external data
6. Ensure SECRET_KEY is from environment in production
7. Add security checklist to README
```

#### 5.4.2 Create Requirements File

```bash
# Generate requirements.txt
pip freeze > requirements.txt
```

Or use Copilot Chat:

```
Create requirements.txt with all dependencies and their versions:
- Flask
- requests
- pytest
- pytest-mock
- pytest-cov
- python-dotenv
Include comments for different sections (production, development, testing)
```

**✓ Checkpoint:** requirements.txt created with all dependencies.

---

## 🎓 Final Project Review & Demo Preparation

### Step 5.5: Final Polish and Testing (10 minutes)

#### 5.5.1 Complete Application Checklist

Use Copilot Chat:

```
Review the entire Flask JokeApp and create a checklist verifying:
1. All routes have error handling
2. All functions have docstrings
3. Tests cover main functionality
4. No hardcoded secrets or API keys
5. Responsive design works on mobile
6. All template links work correctly
7. Logging is properly configured
8. Input validation is in place
9. Error messages are user-friendly
10. Code follows Python best practices (PEP 8)
```

#### 5.5.2 Run Final Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html
```

#### 5.5.3 Final Manual Testing

Test these scenarios:

1. ✅ Home page loads and looks professional
2. ✅ Navigation works on all pages
3. ✅ Get random joke from home page
4. ✅ Select specific category
5. ✅ Custom joke form with filters
6. ✅ Error handling for invalid input
7. ✅ Responsive on mobile/tablet
8. ✅ Footer links work

---

### Step 5.6: Demo Preparation (10 minutes)

#### Prepare Your Demo Script

**1. Introduction (30 seconds)**

- "I built JokeApp using Flask, GitHub Copilot, and JokeAPI"

**2. Features Demo (2 minutes)**

- Show home page and navigation
- Get a random joke
- Select Programming category joke
- Use custom form with filters
- Demonstrate error handling (invalid category)

**3. Technical Highlights (1 minute)**

- Show project structure
- Explain service layer separation
- Show test results
- Mention configuration and logging

**4. GitHub Copilot Usage (1 minute)**

- Explain how Copilot helped generate code
- Show examples of prompts used
- Discuss code review and validation

**✓ Checkpoint:** You can confidently demo your JokeApp in 5 minutes!

---

## 🎉 Final Project Summary

### What You've Built

A complete, production-ready Flask web application with:

**Frontend:**

- ✅ Responsive multi-page layout with Bootstrap
- ✅ Dynamic joke display
- ✅ Interactive forms with validation
- ✅ Professional styling and UX

**Backend:**

- ✅ RESTful routes
- ✅ External API integration
- ✅ Service layer architecture
- ✅ Comprehensive error handling
- ✅ Input validation and sanitization

**Quality Assurance:**

- ✅ Unit tests with pytest
- ✅ Test coverage reports
- ✅ Logging system
- ✅ Documentation (docstrings, README)

**DevOps:**

- ✅ Configuration management
- ✅ Environment variables
- ✅ Security best practices
- ✅ Requirements management

---

## 📊 Skills Mastered

### GitHub Copilot Skills

- ✅ Using Copilot Chat for code generation
- ✅ Providing effective prompts
- ✅ Reviewing and validating AI-generated code
- ✅ Iterative development with Copilot
- ✅ Using Copilot for testing and documentation

### Flask Development Skills

- ✅ Application structure and organization
- ✅ Routing and templates
- ✅ API integration
- ✅ Form handling
- ✅ Error handling
- ✅ Configuration management

### Software Engineering Skills

- ✅ Service layer architecture
- ✅ Unit testing
- ✅ Input validation
- ✅ Logging
- ✅ Documentation
- ✅ Security best practices

---

## 🚀 Next Steps & Extensions

### Suggested Enhancements

1. **Database Integration:**
   - Store favorite jokes
   - User accounts
   - Vote on jokes

2. **Advanced Features:**
   - Search functionality
   - Share jokes on social media
   - Save joke history
   - Random joke of the day

3. **Deployment:**
   - Deploy to Heroku, Railway, or PythonAnywhere
   - Set up CI/CD with GitHub Actions
   - Add Docker containerization

4. **API Development:**
   - Create your own REST API endpoints
   - Add rate limiting
   - Implement caching

5. **Frontend Enhancement:**
   - Add JavaScript for dynamic loading
   - Implement AJAX for smoother UX
   - Add animations and transitions

---

## 📚 Additional Learning Resources

### Flask

- **Official Documentation:** https://flask.palletsprojects.com/
- **Flask Mega-Tutorial:** https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

### Testing

- **pytest Documentation:** https://docs.pytest.org/
- **Testing Flask Applications:** https://flask.palletsprojects.com/en/latest/testing/

### GitHub Copilot

- **Copilot Documentation:** https://docs.github.com/en/copilot
- **Prompt Engineering Guide:** https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/

### APIs

- **REST API Design:** https://restfulapi.net/
- **HTTP Status Codes:** https://httpstatuses.com/

---

## 🎓 Certificate Readiness

You're now ready to:

- ✅ Build Flask web applications independently
- ✅ Integrate external APIs effectively
- ✅ Use GitHub Copilot productively
- ✅ Write tested, documented, production-ready code
- ✅ Follow software engineering best practices

---

## 💬 Feedback & Reflection

### Reflection Questions

1. What was the most challenging part of this project?
2. How did GitHub Copilot help or hinder your development?
3. What would you do differently if starting over?
4. What feature are you most proud of?
5. What will you build next?

### Course Feedback

Please provide feedback on:

- Content clarity and organization
- Pace and difficulty level
- Hands-on exercises
- GitHub Copilot integration
- Instructor support
- Suggestions for improvement

---

## 🎊 Congratulations!

**You've successfully completed the GitHub Copilot with Python Flask course!**

You've built a real-world web application, learned professional development practices, and mastered AI-assisted coding with GitHub Copilot.

**Keep coding, keep learning, and keep building amazing things!** 🚀

---

### 📧 Stay Connected

- Share your JokeApp on GitHub
- Connect with fellow participants
- Join Flask and Python communities
- Continue your learning journey

**Thank you for participating! Happy coding! 🎉👏**
