from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    app.logger.info('Index page accessed')
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.info('Login page accessed')
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    app.logger.info('Logout page accessed')
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(port=5002, debug=True)