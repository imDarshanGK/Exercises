student_marks = {
    "Ram": 78,
    "Mosh": 98,
    "Shyam": 67,
    "John": 56,
    "Tata": 32,
    "Sita": 85,
    "Ravi": 92,
    "Anita": 45,
    "Raj": 74,
    "Geeta": 66,
    "Ali": 58,
    "Nina": 82,
    "Kumar": 34,
    "Sara": 77,
    "Vikram": 89,
    "Priya": 63,
    "Amit": 91
}

student_grade = {}
for student in student_marks:
    marks = student_marks[student]
    if marks >= 90:
        student_grade[student] = "A+"
    elif marks >= 80:
        student_grade[student] = "A"
    elif marks >= 70:
        student_grade[student] = "B+"
    elif marks >= 60:
        student_grade[student] = "B"
    elif marks >= 50:
        student_grade[student] = "C"
    elif marks >= 35:
        student_grade[student] = "D"
    else:
        student_grade[student] = "F"
        
print(student_grade)
