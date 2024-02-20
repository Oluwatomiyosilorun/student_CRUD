from fastapi import FastAPI, HTTPException

app = FastAPI()

students_db = {}


class Student:
    def __init__(self, name: str, age: int, sex: str, height: float):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


# Create a Student
@app.post("/students/")
def create_student(name: str, age: int, sex: str, height: float):
    student_id = len(students_db) + 1
    student = Student(name=name, age=age, sex=sex, height=height)
    students_db[student_id] = student
    return {"id": student_id, "name": name, "age": age, "sex": sex, "height": height}


# Get all students
@app.get("/students/")
def read_students():
    return [{"id": student_id, "name": student.name, "age": student.age, "sex": student.sex, "height": student.height}
            for student_id, student in students_db.items()]


# Get a specific student by ID
@app.get("/students/{student_id}")
def read_students(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return [{"id": student_id, "name": student.name, "age": student.age, "sex": student.sex, "height": student.height}]


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    updated_student = Student(name=name, age=age, sex=sex, height=height)
    students_db[student_id] = updated_student
    return {"id": student_id, "name": name, "age": age, "sex": sex, "height": height}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"id": student_id, "name": student.name, "age": student.age, "sex": student.sex, "height": student.height}
