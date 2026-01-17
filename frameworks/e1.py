#!/usr/bin/env python3
"""e1.py

An example file for a random python framework.

Framework: Flask
Why Flask?
- Lightweight and minimalistic - perfect for learning
- Easy to set up with minimal boilerplate code
- Excellent documentation and large community
- Great for small projects and APIs
- Follows the "micro" framework philosophy - gives you the basics
  and lets you add what you need

"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Return a welcome message."""
    return "Hello, World!"


@app.route("/api/greeting/<name>")
def greeting(name):
    """Return a personalized greeting as JSON."""
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True)
