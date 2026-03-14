students = {
    "Alice": [8, 7, 9],
    "Bob": [6, 5, 7],
    "Charlie": [4, 6, 5]
}

def get_average_grades(grades):
    return sum(grades) / len(grades)

def add_student(student_dict, name, grades):
    student_dict[name] = grades

def print_all_averages(student_dict):
    for student, grades in student_dict.items():
        print(f"Average grade for {student}: {get_average_grades(grades)}")

def get_best_student(student_dict):
    return max(student_dict, key=lambda x: get_average_grades(student_dict[x]))

def get_passed_students(student_dict):
    return [student for student, grades in student_dict.items() if get_average_grades(grades) >= 6]

add_student(students, "David", [10, 10, 10])

print_all_averages(students)

bestStudent = get_best_student(students)
print(f"Best student: {bestStudent}")

passedStudents = get_passed_students(students)
print(f"Passed students: {len(passedStudents)}")