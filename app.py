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

@app.route('/About')
def About_Page():
    """About Page."""

    return render_template('About.html')

@app.route('/Credits')
def Credits_Page():
    """Credits Page."""

    return render_template('Credits.html')

@app.route('/Episode-001')
def Episode001():
    """Episode001: Anglerfish"""

    return render_template('Episode001.html')

@app.route('/Episode-002')
def Episode002():
    """Episode002: Do Not Open"""

    return render_template('Episode002.html')

@app.route('/Episode-003')
def Episode003():
    """Episode003: Across The Street"""

    return render_template('Episode003.html')

@app.route('/Episode-004')
def Episode004():
    """Episode004: Pageturner"""

    return render_template('Episode004.html')

@app.route('/Episode-005')
def Episode005():
    """Episode005: Thrown Away"""

    return render_template('Episode005.html')

@app.route('/Episode-006')
def Episode006():
    """Episode006: Squirm"""

    return render_template('Episode006.html')

@app.route('/Episode-007')
def Episode007():
    """Episode007: The Piper"""

    return render_template('Episode007.html')

@app.route('/Episode-008')
def Episode008():
    """Episode008: Burned Out"""

    return render_template('Episode008.html')

@app.route('/Episode-009')
def Episode009():
    """Episode009: A Father's Love"""

    return render_template('Episode009.html')

@app.route('/Episode-010')
def Episode010():
    """Episode010: Vampire Killer"""

    return render_template('Episode010.html')

@app.route('/Episode-011')
def Episode011():
    """Episode011: Dreamer"""

    return render_template('Episode011.html')

@app.route('/Episode-012')
def Episode012():
    """Episode012: First Aid"""

    return render_template('Episode012.html')

@app.route('/Episode-013')
def Episode013():
    """Episode013: Alone"""

    return render_template('Episode013.html')

@app.route('/Episode-014')
def Episode014():
    """Episode014: Piecemeal"""

    return render_template('Episode014.html')

@app.route('/Episode-015')
def Episode015():
    """Episode015: Lost Johns' Cave"""

    return render_template('Episode015.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
