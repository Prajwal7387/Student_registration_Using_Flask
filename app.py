from flask_cors import CORS
from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__)
CORS(app)

students = []
next_id = 1


def find_student(student_id):
    return next((s for s in students if s["id"] == student_id), None)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({"students": students})


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    student = find_student(student_id)

    if not student:
        abort(404)

    return jsonify(student)


@app.route("/students", methods=["POST"])
def create_student():

    global next_id
    data = request.get_json()

    if not data or not data.get("name"):
        abort(400)

    student = {
        "id": next_id,
        "name": data["name"],
        "email": data.get("email", ""),
        "course": data.get("course", ""),
        "year": data.get("year", "")
    }

    students.append(student)
    next_id += 1

    return jsonify(student), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    student = find_student(student_id)

    if not student:
        abort(404)

    students.remove(student)

    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(debug=True)

    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)