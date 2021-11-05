class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_st_for_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in lecturer.courses_attached) and (
                (course in self.finished_courses) or (course in self.courses_in_progress)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def ever_rat(self):
        s = 0
        k = 0
        for i in self.grades.values():
            for j in i:
                s += j
                k += 1
        return (s / k)

    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.ever_rat()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return a


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(self, name)
        self.grades = {}

    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ever_rat()}'
        return a


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(self, name)

    def rate_rv(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and (
                course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Студент не занимается на данном курсе'

    def __str__(self):
        a = f'Имя: {self.name}'
        return a


student_1 = Student('kobe', 'braynt', 'man')
student_1.finished_courses += ['git']
student_1.courses_in_progress += ['Python']

student_2 = Student('lebron', 'james', 'man')
student_2.finished_courses += ['git']
student_2.courses_in_progress += ['Python']

reviewer_1 = Reviewer('Derrice', 'Rose')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['git']

reviewer_2 = Reviewer('Melo', 'Antony')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['git']

lector_1 = Lecturer('Reggi', 'Miller')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['git']

lector_2 = Lecturer('Dwane', 'Wade')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['git']

reviewer_1.rate_rv(student_1, 'git', 8)
reviewer_1.rate_rv(student_2, 'Python', 10)
reviewer_2.rate_rv(student_1, 'git', 7)
reviewer_2.rate_rv(student_2, 'Python', 9)

student_1.rate_st_for_lect(lector_1, 'git', 7)
student_1.rate_st_for_lect(lector_1, 'Python', 9)
student_2.rate_st_for_lect(lector_2, 'git', 8)
student_2.rate_st_for_lect(lector_2, 'Python', 10)

# print(student_1)
# print(student_2)
print(reviewer_1)
# print(reviewer_2)
# print(lector_1)
# print(lector_2)
