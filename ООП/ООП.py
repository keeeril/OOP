class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_grade(self):
        summa_grades = 0
        for i in self.grades.values():
            summa_grades += i
        return(summa_grades/len(self.grades))

    def __str__(self):
        new = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.aver_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return  new

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)
        self.grades = {}

    def aver_grade(self):
        summa_grades = 0
        for i in self.grades.values():
            summa_grades += i
        return(summa_grades/len(self.grades))

    def __str__(self):
        new = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_grade()}'
        return new

    def __lt__(self, other):
        student = f'Средняя оценка за дз: {other.aver_grade}'
        lecturer = f'Средняя оценка за курс: {self.aver_grade}'
        return student > lecturer

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        new = f'Имя: {self.name}\nФамилия: {self.surname}'
        return new

student_1 = Student('Kirill', 'Polonikov', 'man')
student_1.finished_courses += ['git']
student_1.courses_in_progress += ['Python']

student_2 = Student('Amet', 'Anisjv', 'man')
student_2.finished_courses += ['git']
student_2.courses_in_progress += ['Python']

reviewer_1 = Reviewer('Faina', 'Il')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['git']

reviewer_2 = Reviewer('Metko', 'St')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['git']

lector_1 = Lecturer('Nastia', 'Solovey')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['git']

lector_2 = Lecturer('Lera', 'Pod')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['git']

reviewer_1.rate_hw(student_1, 'git', 8)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'git', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.grade_lecture(lector_1, 'git', 7)
student_1.grade_lecture(lector_1, 'Python', 9)
student_2.grade_lecture(lector_2, 'git', 8)
student_2.grade_lecture(lector_2, 'Python', 10)


print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lector_1)
print(lector_2)

# student = [student_1, student_2]
# не понимаю как реализовать тут функцию.
# def aver_grade_course(student, course):

