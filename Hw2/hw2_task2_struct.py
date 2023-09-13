# Задача 2
# __
# Допустим, у нас есть задача по обработке данных о студентах в университете. 
# У нас есть следующие данные:
# __
# Список студентов с их именами и оценками.
# Нам нужно найти средний балл по всем студентам и вывести имена студентов, 
# чей балл выше среднего.

# Реализация структурного программирования 

# Список студентов
student_data = [
{'name': 'Alice', 'score': 85},
{'name': 'Bob', 'score': 92},
{'name': 'Charlie', 'score': 78},
{'name': 'David', 'score': 95},
]

sum = 0

for student in student_data:
    sum = sum + int(student['score'])
    average = sum / len(student_data)

best_students = []
for student in student_data:
    if int(student['score']) > average:
        best_students.append(student['name'])
        
print(f"Best students: {best_students}")