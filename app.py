import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    # Insecure Configuration: Enabling debug mode in production
    app.config['DEBUG'] = True
    return "Welcome!"

@app.route('/how are you')
def hello():
    # Command Injection: Using os.system with unsanitized input
    name = request.args.get('name')
    os.system(f'echo {name}')
    return f'I am good, how about you, {name}?'

@app.route('/search')
def search():
    # SQL Injection: Simulating a vulnerable SQL query
    query = request.args.get('query')
    sql_query = f"SELECT * FROM users WHERE name = '{query}'"
    # In a real application, this would be an insecure database query
    return f"Searching for: {sql_query}"

@app.route('/xss')
def xss():
    # Cross-Site Scripting (XSS): Returning unsanitized user input
    user_input = request.args.get('input')
    return f"<h1>{user_input}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
