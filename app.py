from flask import Flask, render_template, request, redirect, url_for
import requests
from bson.objectid import ObjectId
import os
from random import randint

app = Flask(__name__)

@app.route('/')
def landing_page():
    """Landing Page."""
    # Displays the landing page. The user can click on the episodes they want.
    return render_template('index.html')

@app.route('/Episode-001')
def Episode001():
    """Episode001: Anglerfish"""
    # Displays the landing page. The user can click on the episodes they want.
    return render_template('Episode001.html')

@app.route('/Episode-002')
def Episode002():
    """Episode002: Do Not Open"""
    # Displays the landing page. The user can click on the episodes they want.
    return render_template('Episode002.html')

@app.route('/Episode-003')
def Episode003():
    """Episode003: Across The Street"""
    # Displays the landing page. The user can click on the episodes they want.
    return render_template('Episode003.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
