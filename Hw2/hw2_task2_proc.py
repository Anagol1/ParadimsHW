# Задача 2
# __
# Допустим, у нас есть задача по обработке данных о студентах в университете. 
# У нас есть следующие данные:
# __
# Список студентов с их именами и оценками.
# Нам нужно найти средний балл по всем студентам и вывести имена студентов, 
# чей балл выше среднего.

# Реализация процедурного программирования 


def calculate_class_average(students):
    total_score = 0
    total_students = len(students)

    for student in students:
        total_score = total_score + int(student['score'])

    return total_score / total_students

def show_best_students(students):
    best_students = []
    for student in students:
        if int(student['score']) > calculate_class_average(students):
            best_students.append(student['name'])
    return best_students

# Список студентов
student_data = [
{'name': 'Alice', 'score': 85},
{'name': 'Bob', 'score': 92},
{'name': 'Charlie', 'score': 78},
{'name': 'David', 'score': 95},
]

print(f"Best students: {show_best_students(student_data)}")



