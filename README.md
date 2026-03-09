# Student Registration System using Flask

## Overview

This project is a simple **Student Registration System** built using **Flask (Python)**. It demonstrates how to build a basic **REST API with CRUD operations** and connect it to a simple **HTML frontend**.

The system allows users to:

* Add students
* View all students
* View a single student
* Delete students

The frontend communicates with the Flask backend using **Fetch API**.

---

# Technologies Used

* Python
* Flask
* Flask-CORS
* HTML
* JavaScript (Fetch API)
* Thunder Client / Postman (for API testing)

---

# Project Structure

```
Student_registration
│
├── venv
├── app.py
├── templates
│   └── index.html
├── requirements.txt
└── README.md
```

---

# Step 1: Create Project Folder

```
mkdir Student_registration
cd Student_registration
```

---

# Step 2: Create Virtual Environment

Create a Python virtual environment.

```
python -m venv venv
```

This creates a folder named **venv**.

---

# Step 3: Activate Virtual Environment

### Windows

```
venv\Scripts\activate
```

Terminal will show:

```
(venv)
```

---

# Step 4: Install Required Packages

Install Flask and Flask-CORS.

```
pip install flask
pip install flask-cors
```

---

# Step 5: Save Dependencies

```
pip freeze > requirements.txt
```

---

# Step 6: Create Flask Backend

Create a file:

```
app.py
```

The backend provides REST API endpoints for managing students.

Features:

* GET all students
* GET single student
* POST create student
* DELETE student

Students are stored temporarily in a Python list.

---

# Step 7: Create Frontend

Create a folder:

```
templates
```

Inside it create:

```
index.html
```

Flask automatically loads HTML files from the **templates** folder using `render_template()`.

---

# Step 8: Connect HTML with Flask

Inside `app.py` add:

```
@app.route("/")
def home():
    return render_template("index.html")
```

Now the frontend will load from:

```
http://127.0.0.1:5000
```

---

# Step 9: Run the Flask Application

Start the server:

```
python app.py
```

Output:

```
Running on http://127.0.0.1:5000
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# Step 10: API Endpoints

## Get All Students

```
GET /students
```

Example:

```
http://127.0.0.1:5000/students
```

---

## Get One Student

```
GET /students/<id>
```

Example:

```
/students/1
```

---

## Create Student

```
POST /students
```

JSON Body Example:

```
{
 "name": "Rahul Sharma",
 "email": "rahul@gmail.com",
 "course": "Computer Science",
 "year": "2"
}
```

---

## Delete Student

```
DELETE /students/<id>
```

Example:

```
/students/1
```

---

# Step 11: Testing API using Thunder Client

Install **Thunder Client** extension in VS Code.

Test the endpoints:

### Create Student

Method: POST

```
http://127.0.0.1:5000/students
```

Add JSON body.

---

### Get All Students

Method: GET

```
http://127.0.0.1:5000/students
```

---

# Step 12: Frontend Functionality

The HTML page allows users to:

* Add students
* Display students in a table
* Delete students

Frontend communicates with Flask using:

```
fetch()
```

---

# Step 13: Important Note

Student data is stored in memory:

```
students = []
```

So when the server restarts, the data will reset.

For permanent storage, a database like **SQLite** can be used.

---

# Step 14: Push Project to GitHub

Initialize Git:

```
git init
```

Add files:

```
git add .
```

Commit:

```
git commit -m "Initial commit - Flask Student Registration"
```

Connect GitHub repository:

```
git remote add origin https://github.com/Prajwal7387/Student_registration_Using_Flask.git
```

Push to GitHub:

```
git branch -M main
git push -u origin main
```

---

# Step 15: .gitignore (Important)

Create a file:

```
.gitignore
```

Add:

```
venv/
__pycache__/
```

This prevents unnecessary files from being uploaded.

---

# Final Result

The project demonstrates:

* Flask REST API
* CRUD Operations
* HTML Frontend
* API Testing with Thunder Client
* GitHub Version Control

---

# Author

Prajwal Mahamuni
