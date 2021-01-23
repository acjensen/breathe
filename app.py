import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def main():
    return render_template('main.html', words='This is the main page.')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
