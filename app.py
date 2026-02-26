from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# JSON file to store courses
DATA_FILE = "courses.json"

# Allowed status values
VALID_STATUS = ["Not Started", "In Progress", "Completed"]


# ---------------------------------------------------
# Utility Functions
# ---------------------------------------------------

def initialize_file():
    """
    Creates courses.json if it does not exist.
    """
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump([], file)
        except Exception as e:
            print("Error creating file:", str(e))


def load_courses():
    """
    Loads courses from JSON file.
    Returns empty list if file read fails.
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        return []


def save_courses(courses):
    """
    Saves course list to JSON file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(courses, file, indent=4)
        return True
    except Exception:
        return False


def generate_new_id(courses):
    """
    Generates next ID automatically.
    """
    if not courses:
        return 1
    return max(course["id"] for course in courses) + 1


def validate_course_data(data, is_update=False):
    """
    Validates incoming request data.
    If is_update=True, only validates provided fields.
    """
    required_fields = ["name", "description", "target_date", "status"]

    if not is_update:
        for field in required_fields:
            if field not in data:
                return f"Missing required field: {field}"

    # Validate status if provided
    if "status" in data:
        if data["status"] not in VALID_STATUS:
            return "Invalid status value. Must be: Not Started, In Progress, or Completed"

    # Validate date format if provided
    if "target_date" in data:
        try:
            datetime.strptime(data["target_date"], "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use YYYY-MM-DD"

    return None


# ---------------------------------------------------
# API ROUTES
# ---------------------------------------------------

# POST /api/courses - Add a new course
@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Validate data
    error = validate_course_data(data)
    if error:
        return jsonify({"error": error}), 400

    courses = load_courses()

    new_course = {
        "id": generate_new_id(courses),
        "name": data["name"],
        "description": data["description"],
        "target_date": data["target_date"],
        "status": data["status"],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    courses.append(new_course)

    if not save_courses(courses):
        return jsonify({"error": "Failed to save course"}), 500

    return jsonify(new_course), 201


# GET /api/courses - Get all courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = load_courses()
    return jsonify(courses), 200


# GET /api/courses/<id> - Get specific course
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    courses = load_courses()

    for course in courses:
        if course["id"] == course_id:
            return jsonify(course), 200

    return jsonify({"error": "Course not found"}), 404


# PUT /api/courses/<id> - Update a course
@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Validate update data
    error = validate_course_data(data, is_update=True)
    if error:
        return jsonify({"error": error}), 400

    courses = load_courses()

    for course in courses:
        if course["id"] == course_id:
            course.update(data)

            if not save_courses(courses):
                return jsonify({"error": "Failed to update course"}), 500

            return jsonify(course), 200

    return jsonify({"error": "Course not found"}), 404


# DELETE /api/courses/<id> - Delete a course
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    courses = load_courses()

    updated_courses = [course for course in courses if course["id"] != course_id]

    if len(updated_courses) == len(courses):
        return jsonify({"error": "Course not found"}), 404

    if not save_courses(updated_courses):
        return jsonify({"error": "Failed to delete course"}), 500

    return jsonify({"message": "Course deleted successfully"}), 200


# ---------------------------------------------------
# Run Application
# ---------------------------------------------------

if __name__ == "__main__":
    initialize_file()  # Automatically create courses.json if missing
    app.run(debug=True)