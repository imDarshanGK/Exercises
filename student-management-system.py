student_data = [
    {
        "Name" : "Vijay",
        "roll_no" : 13,
        "age" : 23,
        "course" : "Python"
    },
    
    {
        "Name" : "Ragu",
        "roll_no" : 14,
        "age" : 25,
        "course" : "R"
    }
]
def add_new_student(name,rollno,age,course):
    new_student={}
    new_student["Name"] = name
    new_student["roll_no"] = rollno
    new_student["age"] = age
    new_student["course"] = course
    student_data.append(new_student)
    
add_new_student("shiva",17,16,"jave")
print(student_data)
