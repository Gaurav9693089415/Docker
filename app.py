from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Docker Demo App</title>
        </head>
        <body>
            <h1>Welcome to Docker Demo App</h1>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username" required>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form.get('username', 'Guest')  # Default to 'Guest' if username not provided
    return f'''
        <html>
        <head>
            <title>Greetings</title>
        </head>
        <body>
            <h1>Hello {username}!</h1>
            <p>Welcome to this app for Docker demonstration.</p>
            <p>Please consider like and subscribe to the channel.</p>
            <a href="/">Back to Home</a>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)