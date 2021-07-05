class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finish_courses = []
        self.cours_progres = []
        self.grade = {}
        self.average_score = 0
        students_list.append(self.__dict__)

    def rate_lecture(self, lektor, course, grade):
        if isinstance(lektor, Lecturer) and course in self.cours_progres and course in lektor.courses_attached:
            lektor.grades += [grade]
            lektor.average_score = round(sum(lektor.grades) / len(lektor.grades), 2)


    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_score < other.average_score

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_score} \n' \
               f'Курсы в процессе изучения: {self.cours_progres} \n' \
               f'Завершенные курсы: {self.finish_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        self.grades = []
        self.average_score = 0
        super().__init__(name, surname)
        lektors_list.append(self.__dict__)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average_score}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_score < other.average_score

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.cours_progres:
            if course in student.grade:
                student.grade[course] += [grade]
            else:
                student.grade[course] = [grade]
            sum_hw = 0
            counter = 0
            for key, value in student.grade.items():
                sum_hw += sum(value) / len(value)
                counter += 1
            student.average_score = round(sum_hw / counter, 2)


    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}'

students_list = []
lektors_list = []

def average_grade_hw(students, courses):
    sum_gh = 0
    counter = 0
    for student in students:
        for key, value in student['grades'].items():
            if courses in key:
                sum_gh += sum(value) / len(value)
                counter += 1
    return round(sum_gh / counter, 2)



def average_grade_lecture(lecturers, courses):
    sum_gl = 0
    counter = 0
    for lector in lecturers:
        if courses in lector["courses_attached"]:
           sum_gl += sum(lector["grades"]) / len(lector["grades"])
           counter += 1
    return round(sum_gl / counter, 2)



nikolaev = Student('Николай', 'Николаев', 'м')
nikolaev.cours_progres += ['Математика']
nikolaev.cours_progres += ['Электроника']

savin = Student('Константин', 'Савин', 'м')
savin.cours_progres += ['Электроника']
savin.finish_courses += ['Математика']

strapenin = Lecturer('Григорий', 'Страпенин')
strapenin.courses_attached += ['Электроника']

bautin = Lecturer('Петр', 'Баутин')
bautin.courses_attached += ['Математика']

sadov = Reviewer('Андрей', 'Садов')
sadov.courses_attached += ['Математика']

lisin = Reviewer('Валерий', 'Лисин')
lisin.courses_attached += ['Электроника']


sadov.rate_hw(nikolaev, 'Математика', 4)
sadov.rate_hw(nikolaev, 'Математика', 4)
sadov.rate_hw(nikolaev, 'Математика', 4)
sadov.rate_hw(savin, 'Математика', 5)

lisin.rate_hw(nikolaev, 'Электроника', 3)
lisin.rate_hw(nikolaev, 'Электроника', 4)
lisin.rate_hw(nikolaev, 'Электроника', 5)
lisin.rate_hw(savin, 'Электроника', 3)
lisin.rate_hw(savin, 'Электроника', 3)
lisin.rate_hw(savin, 'Электроника', 3)

nikolaev.rate_lecture(strapenin, 'Электроника', 7)
nikolaev.rate_lecture(strapenin, 'Электроника', 8)
nikolaev.rate_lecture(strapenin, 'Электроника', 5)
savin.rate_lecture(strapenin, 'Электроника', 2)
savin.rate_lecture(strapenin, 'Электроника', 1)
savin.rate_lecture(strapenin, 'Электроника', 1)

nikolaev.rate_lecture(bautin, 'Математика', 9)
nikolaev.rate_lecture(bautin, 'Математика', 7)
nikolaev.rate_lecture(bautin, 'Математика', 6)

savin.rate_lecture(bautin, 'Математика', 8)

print(f'')
print(nikolaev)
print(f'')
print(savin)
print(f'')
print(bautin)
print(f'')
print(strapenin)
print(f'')
print(sadov)
print(f'')
print(lisin)

print(f'')
print("Средний балл за домашние задания по курсу:", average_grade_hw(students_list, 'Электроника'))
print("Средний балл за лекции по курсу:", average_grade_lecture(lektors_list, 'Математика'))

print(f'')
print(strapenin > bautin)
print(f'')
print(nikolaev > savin)