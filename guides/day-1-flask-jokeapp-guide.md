# Day 1: Getting Started with GitHub Copilot & Building Flask Application

**Duration:** 3.5 Hours  
**Modules Covered:**

- Module 1: Getting Started with GitHub Copilot & Flask (1.5 hrs)
- Module 2: Building Flask Application Structure (2 hrs)

---

## 🎯 Learning Objectives

By the end of Day 1, you will be able to:

- ✅ Set up Python development environment with Flask and GitHub Copilot
- ✅ Use GitHub Copilot Chat effectively for code generation
- ✅ Create a Flask application with multiple routes
- ✅ Build templates using Jinja2 with Bootstrap
- ✅ Organize static files (CSS, JS) in Flask
- ✅ Create a multi-page web application with navigation

---

## 📋 Pre-requisites

Before starting, ensure you have:

- Basic Python knowledge (functions, loops, imports)
- Basic HTTP concepts (requests, responses)
- GitHub account with Copilot access enabled
- VS Code installed
- Python 3.8+ installed

---

## Module 1: Getting Started with GitHub Copilot & Flask (1.5 hours)

### Step 1.1: Environment Setup (15 minutes)

#### 1.1.1 Verify Python Installation

```bash
python --version
# Should show Python 3.8 or higher
```

#### 1.1.2 Install VS Code Extensions

1. Open VS Code
2. Install the following extensions:
   - **Python** (Microsoft)
   - **GitHub Copilot**
   - **GitHub Copilot Chat**
3. Sign in to GitHub Copilot

#### 1.1.3 Create Project Structure

```bash
# Create project directory
mkdir flask-jokeapp
cd flask-jokeapp

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install Flask
pip install flask
```

**✓ Checkpoint:** Your terminal prompt should show `(venv)` indicating the virtual environment is active.

---

### Step 1.2: Introduction to GitHub Copilot (20 minutes)

#### 1.2.1 Understanding Copilot Features

GitHub Copilot assists with:

- **Inline suggestions:** Auto-completes code as you type
- **Multi-line completions:** Generates entire functions/blocks
- **Comment-driven development:** Generates code from descriptive comments

#### 1.2.2 Copilot Chat Warm-up Exercise

1. Open Copilot Chat panel: `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
2. Try these prompts to get familiar:

**Prompt 1:**

```
Create a Python function that adds two numbers and returns the result
```

**Prompt 2:**

```
Write a function that calls a public REST API and returns parsed JSON data with error handling
```

**🔍 Review Rule:** Always review generated code before accepting. Check for:

- Correctness and logic
- Security implications
- Code style and readability

---

### Step 1.3: Create Your First Flask App (30 minutes)

#### 1.3.1 Generate Basic Flask Application

Open Copilot Chat and use this prompt:

```
Create a Flask application in app.py with:
- A single route at / that returns "Hello, JokeApp!"
- Debug mode enabled
- A /health route that returns JSON with status: ok
- Docstrings for all functions
- Run on host 0.0.0.0 and port 5000
```

**Expected Output:** `app.py` file with basic Flask setup

#### 1.3.2 Understanding the Generated Code

Review the generated `app.py` and understand:

- `from flask import Flask` - Importing Flask
- `app = Flask(__name__)` - Creating Flask app instance
- `@app.route('/')` - Decorator for routing
- `if __name__ == '__main__':` - Running the app

#### 1.3.3 Run Your First Flask App

```bash
# Method 1: Using flask command
flask run

# Method 2: Direct execution
python app.py
```

**Visit:** http://127.0.0.1:5000/

**✓ Checkpoint:**

- Browser shows "Hello, JokeApp!"
- Visiting http://127.0.0.1:5000/health returns JSON: `{"status": "ok"}`

---

### Step 1.4: Understanding Flask Basics (25 minutes)

#### 1.4.1 Routes and HTTP Methods

Use Copilot Chat to add a new route:

```
Add a route /greet/<name> to app.py that returns a personalized greeting.
Use f-strings for the message.
```

**Test it:** Visit http://127.0.0.1:5000/greet/YourName

#### 1.4.2 Debug Mode and Auto-reload

Modify your greeting message in the code and save. The server automatically reloads!

**Understanding Debug Mode:**

- Auto-reloads on code changes
- Shows detailed error messages
- **WARNING:** Never use debug mode in production

#### 1.4.3 Flask App Structure Best Practices

Use Copilot Chat to understand:

```
Explain the recommended folder structure for a Flask application with templates and static files
```

---

## ☕ Break (10 minutes)

---

## Module 2: Building Flask Application Structure (2 hours)

### Step 2.1: Create Project Structure (30 minutes)

#### 2.1.1 Generate Complete Folder Structure

Use Copilot Chat with this comprehensive prompt:

```
Create a Flask project structure for flask-jokeapp with:
- templates/ folder with base.html (Bootstrap 5 navbar with links to Home/About/Contact)
- templates/home.html, about.html, contact.html (all extending base.html)
- static/ folder with style.css for custom styling
- Update app.py to add routes: / (home), /about, /contact that render these templates
- Use Bootstrap 5 CDN in base.html
- Add a responsive navbar with the app name "JokeApp" and navigation links
- Include a container div in base.html for content blocks
```

#### 2.1.2 Review Generated Files

After Copilot generates the files, review:

**File: `templates/base.html`**

- Bootstrap 5 CDN links
- Navbar structure
- `{% block content %}` and `{% endblock %}` for template inheritance
- Link to static CSS: `{{ url_for('static', filename='style.css') }}`

**File: `templates/home.html`**

- `{% extends "base.html" %}`
- `{% block content %}` ... `{% endblock %}`

**File: `app.py`**

- Import `render_template` from Flask
- Routes using `@app.route()` decorator
- `return render_template('home.html')` pattern

**File: `static/style.css`**

- Custom styles for the application

**✓ Checkpoint:** Run the app and navigate between Home, About, and Contact pages using the navbar.

---

### Step 2.2: Enhance the Home Page (25 minutes)

#### 2.2.1 Create Hero Section

Use Copilot Chat:

```
Update templates/home.html to include:
- A hero section with a large heading "Welcome to JokeApp"
- A subtitle explaining "Get jokes from JokeAPI - Programming, Miscellaneous, and Dark humor"
- A Bootstrap jumbotron/hero style layout
- A primary button "Get Started" (placeholder for now)
```

#### 2.2.2 Add Feature Cards

Use Copilot Chat:

```
Below the hero section in home.html, add a row of 3 Bootstrap cards showcasing:
1. "Random Jokes" - Icon and description
2. "Category Selection" - Icon and description
3. "Custom Filters" - Icon and description
Use Bootstrap icons or emoji for visual appeal
```

**✓ Checkpoint:** Home page now has a professional-looking hero section and feature cards.

---

### Step 2.3: Enhance Navigation and Layout (20 minutes)

#### 2.3.1 Add Footer to Base Template

Use Copilot Chat:

```
Add a footer to base.html with:
- Bootstrap footer styling
- Link to JokeAPI website (https://v2.jokeapi.dev)
- Copyright notice with current year
- Center-aligned text
- Background color matching the navbar
- Sticky footer that stays at bottom
```

#### 2.3.2 Improve About Page

Use Copilot Chat:

```
Update templates/about.html to include:
- Project description explaining the JokeApp purpose
- Technology stack used (Flask, Bootstrap, JokeAPI)
- List of features as Bootstrap list group
- Information about GitHub Copilot's role in building this app
```

#### 2.3.3 Create Contact Page Content

Use Copilot Chat:

```
Update templates/contact.html with:
- A simple contact information section
- Email placeholder
- GitHub repository link placeholder
- Bootstrap card layout
```

**✓ Checkpoint:** All pages have consistent styling, working navigation, and a footer.

---

### Step 2.4: Advanced Styling and Responsiveness (25 minutes)

#### 2.4.1 Enhance Custom CSS

Use Copilot Chat:

```
Update static/style.css to add:
- Custom color scheme (define CSS variables for primary, secondary colors)
- Navbar custom styling with hover effects
- Card hover effects with subtle shadows
- Better typography (font sizes, line heights)
- Responsive breakpoints for mobile devices
- Smooth transitions for interactive elements
```

#### 2.4.2 Test Responsiveness

1. Open browser developer tools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. Test on different screen sizes:
   - Mobile (375px)
   - Tablet (768px)
   - Desktop (1920px)

**🔍 Review:** Ensure navbar collapses to hamburger menu on mobile.

---

### Step 2.5: Understanding Jinja2 Templates (20 minutes)

#### 2.5.1 Template Inheritance Explained

**Prompt Copilot Chat:**

```
Explain Jinja2 template inheritance with examples. Show how extends, block, and include work
```

**Key Concepts:**

- `{% extends "base.html" %}` - Child inherits from parent
- `{% block content %}` - Defines replaceable sections
- `{{ variable }}` - Outputs variable values
- `{% for item in items %}` - Loops
- `{% if condition %}` - Conditionals

#### 2.5.2 Using url_for()

Use Copilot Chat to add:

```
Update the navbar in base.html to use url_for() for all navigation links instead of hardcoded URLs
```

**Why url_for()?**

- Generates URLs dynamically
- Avoids broken links when routes change
- Handles static files correctly

**✓ Checkpoint:** All navigation links use `url_for('route_name')` syntax.

---

### Step 2.6: Adding Dynamic Content (20 minutes)

#### 2.6.1 Pass Variables to Templates

Use Copilot Chat:

```
Update app.py:
- Add a variable app_version = "1.0.0"
- Modify the home route to pass app_version and a welcome message to home.html
- Display these in home.html
- Add current year to footer using a context processor
```

#### 2.6.2 Create a Context Processor

**Prompt:**

```
Add a context processor to app.py that makes current_year available to all templates
Update footer to use {{ current_year }}
```

**Understanding Context Processors:**

- Makes variables available to all templates
- Avoids repeating code in every route
- Useful for common data (year, user info, app config)

**✓ Checkpoint:** Footer displays current year dynamically.

---

## 🎓 Day 1 Summary and Homework

### What You've Learned Today

✅ **Module 1 Achievements:**

- Set up Flask development environment
- Used GitHub Copilot Chat for code generation
- Created and ran your first Flask application
- Understood Flask routing and debug mode

✅ **Module 2 Achievements:**

- Built complete Flask application structure
- Created templates with Jinja2 inheritance
- Implemented Bootstrap for responsive design
- Added navigation, footer, and multiple pages
- Styled application with custom CSS
- Used url_for() for dynamic URLs
- Implemented context processors

### Project Status

Your JokeApp now has:

- ✅ Professional multi-page layout
- ✅ Responsive navigation
- ✅ Bootstrap-styled pages (Home, About, Contact)
- ✅ Custom styling
- ✅ Template inheritance structure
- ✅ Ready for API integration (Day 2!)

---

### 📝 Homework (Optional but Recommended)

1. **Add a New Page:**
   - Create a "Features" page listing all JokeApp capabilities
   - Add it to the navbar
   - Use Bootstrap components

2. **Experiment with Copilot:**
   - Ask Copilot to generate different Bootstrap components
   - Try adding a carousel or modal to the home page

3. **Customize Styling:**
   - Change the color scheme in CSS
   - Add your own custom fonts
   - Experiment with animations

4. **Code Review Exercise:**
   - Review all generated code
   - Add comments explaining what each section does
   - Use Copilot to help generate documentation

---

### 🔍 Self-Assessment Checklist

Before Day 2, ensure you can:

- [ ] Create and activate a Python virtual environment
- [ ] Use GitHub Copilot Chat to generate code
- [ ] Create Flask routes that render templates
- [ ] Understand Jinja2 template inheritance
- [ ] Use Bootstrap classes for styling
- [ ] Organize static files in Flask
- [ ] Use url_for() for links
- [ ] Run and debug a Flask application

---

### 📚 Additional Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **Jinja2 Template Designer:** https://jinja.palletsprojects.com/
- **Bootstrap 5 Documentation:** https://getbootstrap.com/docs/5.0/
- **GitHub Copilot Docs:** https://docs.github.com/en/copilot

---

### 🚀 Preview: Day 2

Tomorrow we'll:

- Integrate JokeAPI to fetch real jokes
- Handle API requests and responses
- Implement error handling
- Add forms for user input
- Refactor code into services
- Write tests with pytest
- Add logging and configuration
- Prepare for production deployment

**Get ready to make your JokeApp functional!** 🎉

---

### 💬 Questions?

Write down any questions or challenges you faced today. We'll address them at the start of Day 2.

---

**Great job completing Day 1! See you tomorrow! 👏**
