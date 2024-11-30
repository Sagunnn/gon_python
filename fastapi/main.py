from fastapi import FastAPI,Path

app = FastAPI()

students={
    1:{
        "name": "John",
        "age":16,
        "class":12
    },
    2:{
        "name": "Jomsom",
        "age":16,
        "class":12
    }
}
@app.get('/')
def index():
    return {"Description":"My first FastAPI application"}

@app.get('/get-student/{student_id}')
def get_student(student_id:int=Path(...,description="Input student ID")):
    return students[student_id]

@app.get('/get-student-by-name/')
def get_student(name : str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Student not found"}