# 10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso,
# escriba un programa que manipule dichas estructuras de datos
# para poder resolver los siguientes puntos:
# A. Generar una estructura con todas las notas relacionando
# el nombre del estudiante con las notas.
# Utilizar esta estructura para la resolución de los siguientes items.
# B. Calcular el promedio de notas de cada estudiante.
# C. Calcular el promedio general del curso.
# D. Identiﬁcar al estudiante con la nota promedio más alta.
# E. Identiﬁcar al estudiante con la nota más baja.
# Nota:
# • Las 3 estructuras están ordenadas de forma que los elementos
# en la misma posición corresponden a un mismo alumno.
# • Realizar funciones con cada item

names = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
grades_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
            12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
            85, 73, 37, 42, 95, 18, 7,
            74, 60, 9, 65, 93, 63, 74]
grades_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
            64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
            95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


# Resuelve A.
def generate_students_grades(names, grades_1, grades_2):
    """
    Creates a dictionary containing the grades of every student

    Parameters:
    names: list of names' students(strings)
    grades_1: grades' list(int) for the students
    grades_2: grades' list(int) for the students

    Returns:
    students_grades_dict: dictionary where each key is a student name and each value is a tuple
    containing the student's grades for his class
    """
    students_grades_dict = {
        name: (grade_1, grade_2)
        for name, grade_1, grade_2
        in zip(names, grades_1, grades_2)
    }
    return students_grades_dict

# Resuelve B.
def calculate_average_per_student(students_grades):
    """
    Calculates the average grade of each student

    Parameters:
    students_grades: dictionary where each key is a student name and each value is a tuple
    containing the student's grades for his class

    Returns:
    average_per_student: dictionary where each key is a student name and each value is the average grade of that student
    calculated from his grades
    """
    average = lambda x: sum(x) / len(x)
    average_grades_list = list(map(average, students_grades.values()))

    average_per_student = {
        student: his_average
        for student, his_average
        in zip(students_grades.keys(), average_grades_list)
    }

    return average_per_student

# Resuelve C.
def calculate_class_average(students_grades):
    """
    Calculates the average grade for the entire class.

    Parameters:
    students_grades: dictionary where each key is a student name and each value is a tuple
    containing the student's grades for his class

    Returns:
    class_average: average grade for the entire class, calculated from the grades of all students
    """
    sum_elements = lambda x: sum(x)
    sum_grades = list(map(sum_elements, students_grades.values()))
    class_average = sum(sum_grades) / len(students_grades)
    return class_average

# Resuelve D.
def calculate_student_with_highest_average(students_grades):
    """
    Calculate the name of the student with the highest average among all the students

    Parameters:
    students_grades: dictionary where each key is a student name and each value is a tuple
    containing the student's grades for his class

    Returns:
    student, average: the name of the student with the highest average grade and that grade
    """
    averages_grades_dict = calculate_average_per_student(students_grades)
    highest_average_student = max(averages_grades_dict.items(), key=lambda x: x[1])
    student = highest_average_student[0]
    average = highest_average_student[1]
    return student, average

# Resuelve E.
def calculate_student_with_lowest_grade(students_grades):
    """
    Calculates the name of the student with the lowest grade in the entire class

    Parameters:
    students_grades: dictionary where each key is a student name and each value is a tuple
    containing the student's grades for his class

    Returns:
    student, lowest_grade: the name of the student with the lowest grade and that grade.
    """
    min_element = lambda x: min(x)
    lowest_grades = list(map(min_element, students_grades.values()))

    lowest_grades_dict = {
        student: his_grade
        for student, his_grade
        in zip(students_grades.keys(), lowest_grades)
    }

    lowest_grade_student = min(lowest_grades_dict.items(), key=lambda x: x[1])
    student = lowest_grade_student[0]
    lowest_grade = lowest_grade_student[1]
    return student, lowest_grade


# limpio string original
students = names.replace(",", "").replace("'", "").title().split()

# A. genero estructura con función
students_grades = generate_students_grades(students, grades_1, grades_2)
print('A. Nombre del estudiante y sus notas:')
for student, his_grades in students_grades.items():
    print(f'{student}: {his_grades}')
print()

# B. calculo el promedio de notas de cada estudiante
average_per_student = calculate_average_per_student(students_grades)
print('B. Promedio de cada alumno:')
for student, his_average in average_per_student.items():
    print(f'{student}: {his_average}')
#print(average_per_student)
print()

# C. calculo promedio del curso
class_average = calculate_class_average(students_grades)
print(f'C. Promedio del curso = {round(class_average,2)}')
print()

# D. identifico al alumno con la nota promedio más alta
student_with_highest_average, highest_average = calculate_student_with_highest_average(students_grades)
print(
    f'D. Alumno con mejor promedio: {student_with_highest_average} (promedio: {highest_average})')
print()

# E. identiﬁco al estudiante con la nota más baja.
student_with_lowest_grade, lowest_grade = calculate_student_with_lowest_grade(students_grades)
print(f'E. Alumno con nota más baja: {student_with_lowest_grade} (nota: {lowest_grade})')