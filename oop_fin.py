class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

 
#Перегрузка метода str
    def __str__(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_grade = sum(map(sum, self.grades.values())) / grades_count
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' + str(round(self.average_grade, 1)) + '\nКурсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\nЗавершенные курсы: ' + ', '.join(self.finished_courses)
        
#Оценка лектора студентами
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

#Сравнение студентов по средней оценке  
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_grade < other.average_grade  

  
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_grade = float()

#Перегрузка метода str
    def __str__(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_grade = sum(map(sum, self.grades.values())) / grades_count
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(round(self.average_grade, 1))

#сравнение лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_grade < other.average_grade


    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Оценка ревьюером домашней работы студента
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname
        


#Создание объектов
student_1 = Student('Петр', 'Иванов', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['C#']
student_1.finished_courses += ['React']

student_2 = Student('Иван', 'Петров', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['C#']
student_2.finished_courses += ['React']

reviewer_1 = Reviewer('Сергей', 'Андреев')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['C#']

reviewer_2 = Reviewer('Андрей', 'Сергеев')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']
reviewer_2.courses_attached += ['C#']

lecturer_1 = Lecturer('Алексей', 'Владимиров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['C#']

lecturer_2 = Lecturer('Владимир', 'Алексеев')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['C#']

#Оценка лекторов студентами
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Java', 9)
student_1.rate_lecture(lecturer_1, 'C#', 10)

student_1.rate_lecture(lecturer_2, 'Python', 9)
student_1.rate_lecture(lecturer_2, 'Java', 8)
student_1.rate_lecture(lecturer_2, 'C#', 10)

student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Java', 8)
student_2.rate_lecture(lecturer_1, 'C#', 9)

student_2.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Java', 10)
student_2.rate_lecture(lecturer_2, 'C#', 9)


#оценка ДЗ студентов
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'C#', 9)

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Java', 8)
reviewer_1.rate_hw(student_2, 'C#', 8)

reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Java', 9)
reviewer_2.rate_hw(student_1, 'C#', 8)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'C#', 9)


#результаты студентов:
print('\n\nРезультаты студентов:')
print(student_1)
print()
print(student_2)

#Результаты лекторов
print('\n\nРезультаты лекторов:')
print(lecturer_1)
print()
print(lecturer_2)

#Сравнение средних оценок студентов за ДЗ
print('\n\nСравнение средних оценок студентов за ДЗ: ')
print(f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')
print()

#Сравнение средних оценок лекторов за лекции
print('Сравнение средних оценок лекторов за лекции: ')
print(f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 < lecturer_2}')
print()

#Список студентов
students = [student_1, student_2]

#Список лекторов
lecturers = [lecturer_1, lecturer_2]


#Функция для подсчета средней оценки за домашние задания
#по всем студентам в рамках конкретного курса
def course_rating_s(students, course_name):
    sum_grade = 0
    count_grade = 0
    course_average = 0
    for st in students:
        if course_name in st.courses_in_progress:
            course_average = sum(st.grades[course_name])/ len(st.grades[course_name])
            sum_grade += course_average
            count_grade += 1
    course_average = sum_grade / count_grade
    return course_average


#Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def course_rating_l(lecturers, course_name):
    sum_grade = 0
    count_grade = 0
    course_average = 0
    for lr in lecturers:
        if  course_name in lr.courses_attached:
            course_average = sum(lr.grades[course_name])/ len(lr.grades[course_name])
            sum_grade += course_average
            count_grade += 1
    course_average = sum_grade / count_grade
    return course_average


#Подсчет средней оценки по всем студентам для данного курса
courses = list(set(student_1.courses_in_progress) & set(student_2.courses_in_progress))
for course in courses:
    print(f"Средняя оценка для всех студентов по курсу {course}: {course_rating_s(students, course)}")
print()

#Подсчет средней оценки по всем лекторам для данного курса
courses = list(set(lecturer_1.courses_attached) & set(lecturer_2.courses_attached))
for course in courses:
    print(f"Средняя оценка для всех лекторов по курсу {course}: {course_rating_l(lecturers, course)}")