📘 CodeCraftHub – Personalized Learning Tracker API
🚀 Project Overview

CodeCraftHub is a simple REST API built using Python and Flask that allows developers to track the courses they want to learn.

This project is designed for beginners who are learning:

REST APIs

CRUD operations

JSON file storage

Backend development basics

No database is used — all data is stored inside a courses.json file.

This makes it perfect for understanding how backend systems work before moving to advanced topics like databases.

🎯 Project Purpose

The goal of this project is to help beginners:

Understand how REST APIs work

Learn HTTP methods (GET, POST, PUT, DELETE)

Work with JSON data

Handle validation and error responses

Practice API testing using Postman, curl, or PowerShell

✨ Features

✔ Create new courses
✔ View all courses
✔ View a specific course by ID
✔ Update course details
✔ Delete a course
✔ Auto-generated course ID
✔ Auto-generated timestamp (created_at)
✔ Input validation
✔ Error handling
✔ JSON file auto-creation

🛠 Installation Instructions (Step-by-Step)
1️⃣ Clone or Create Project Folder

Create a folder named:

CodeCraftHub

Open it in VS Code.

2️⃣ Create Virtual Environment

Open terminal inside VS Code:

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

You should see:

(venv)
3️⃣ Install Flask
pip install Flask
4️⃣ Create Required Files

Your project should contain:

CodeCraftHub
│
├── app.py
├── courses.json
└── README.md

If courses.json does not exist, it will be automatically created when the app runs.

▶️ How to Run the Application

Inside the project folder:

python app.py

You should see:

Running on http://127.0.0.1:5000

The API is now running.

📡 API Endpoints Documentation

Base URL:

http://127.0.0.1:5000
🔹 1. Create a Course

POST /api/courses

Example JSON Body:
{
  "name": "Python Backend",
  "description": "Learn Flask and REST APIs",
  "target_date": "2026-06-01",
  "status": "Not Started"
}
Success Response (201 Created):
{
  "id": 1,
  "name": "Python Backend",
  "description": "Learn Flask and REST APIs",
  "target_date": "2026-06-01",
  "status": "Not Started",
  "created_at": "2026-02-26 21:03:18"
}
🔹 2. Get All Courses

GET /api/courses

Response:

[
  {
    "id": 1,
    "name": "Python Backend",
    "description": "Learn Flask and REST APIs",
    "target_date": "2026-06-01",
    "status": "Not Started",
    "created_at": "2026-02-26 21:03:18"
  }
]
🔹 3. Get Course by ID

GET /api/courses/1

🔹 4. Update Course

PUT /api/courses/1

Example:

{
  "status": "In Progress"
}
🔹 5. Delete Course

DELETE /api/courses/1

Response:

{
  "message": "Course deleted successfully"
}
🧪 Testing Instructions

You can test the API using:

Postman

Thunder Client (VS Code extension)

curl

PowerShell Invoke-RestMethod

Example PowerShell Test
Invoke-RestMethod -Method GET http://127.0.0.1:5000/api/courses
Example curl Test
curl http://127.0.0.1:5000/api/courses
❌ Error Scenarios

The API handles common errors:

Missing Field
{
  "error": "Missing required field: status"
}
Invalid Status
{
  "error": "Invalid status value. Must be: Not Started, In Progress, or Completed"
}
Invalid Date Format
{
  "error": "Invalid date format. Use YYYY-MM-DD"
}
Course Not Found
{
  "error": "Course not found"
}
🛑 Troubleshooting Common Issues
❌ "Unable to connect to server"

Make sure Flask is running:

python app.py
❌ 415 Unsupported Media Type

In Postman:

Select Body

Choose raw

Select JSON

❌ PowerShell curl not working

Use:

curl.exe

instead of just curl.

❌ JSON file not found

No problem. The app creates courses.json automatically.

📂 Project Structure Explanation
CodeCraftHub
│
├── app.py          # Main Flask application
├── courses.json    # Stores course data (acts like a database)
└── README.md       # Project documentation
app.py

Contains:

API routes

Validation logic

File handling

Error handling

courses.json

Stores data in JSON format like:

[
  {
    "id": 1,
    "name": "Python Backend",
    "description": "Learn Flask",
    "target_date": "2026-06-01",
    "status": "Not Started",
    "created_at": "2026-02-26 21:03:18"
  }
]
📚 What You Learned From This Project

REST API basics

HTTP methods

JSON handling

CRUD operations

Validation

Backend structure

API testing

Error handling

🚀 Future Improvements

Add filtering (?status=Completed)

Add search functionality

Add pagination

Add authentication

Connect to a real database (SQLite / PostgreSQL)

Deploy to Render or Railway

🏆 Conclusion

CodeCraftHub is a beginner-friendly REST API project that demonstrates how backend systems work without using a database.

It is a great foundation before moving into:

Advanced Flask

FastAPI

Databases

Authentication systems

Full-stack development