import os
from flask import Flask, render_template, jsonify, redirect
import random
from google.cloud import firestore
from datetime import timezone, datetime, timedelta

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def main():
    return render_template('main.html', words='This is the main page.')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/ping-home')
def ping_home():
    data = {'ping_timestamp': datetime.now(timezone.utc)}
    doc_ref = db.collection(u'active_users').document().set(data)
    return None


@app.route('/num-active-users', methods=['GET'])
def users():
    num_active_users = db.collection(
        u'num_active_users').document(u'num_active_users').get().to_dict()['num_active_users']
    return jsonify({'num_active_users': num_active_users})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
