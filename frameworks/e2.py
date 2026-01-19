# !/usr/bin/env python3
"""e2.py

A python framework example file.
Demonstrates Flask - a popular lightweight web framework.

"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build an API", "completed": False},
]


@app.route("/")
def home():
    """Home route returning a welcome message."""
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks."""
    return jsonify(tasks)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a specific task by ID."""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    """Create a new task."""
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled"),
        "completed": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


if __name__ == "__main__":
    # Run the development server
    app.run(debug=True, port=5000)
