class Mentors:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attach_courses(self, course):
        self.courses_attached.append(course)


class Reviewers(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if grade in range(1, 11):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Неверная оценка, попробуйте  ввести от 1 до 10"

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname} \n__________________________________________________"


class Lectors(Mentors):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grades = {}

    def average_rating_lector(self):
        all_grade = []
        for each_value in self.lector_grades.values():
            for each in each_value:
                all_grade.append(each)
        return sum(all_grade) / len(all_grade)

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {round(self.average_rating_lector(), 2)}"

    def __lt__(self, other):
        if not isinstance(other, Lectors):
            print("not a Lectors")
        return self.average_rating_lector() > other.average_rating_lector()


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if grade in range(1, 11):
            if isinstance(lector, Lectors) and ((course in self.courses_in_progress) or (
                    course in self.finished_courses)) and lector.courses_attached:
                if course in lector.lector_grades:
                    lector.lector_grades[course] += [grade]
                else:
                    lector.lector_grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Неверная оценка, попробуйте  ввести от 1 до 10"

    def average_rating_student(self):
        all_grade1 = []
        for each_value in self.grades.values():
            for each in each_value:
                all_grade1.append(each)
        return (sum(all_grade1) / len(all_grade1))

    def print_list(self, list):
        result = ''
        for each in list:
            result += each + ','
        return result[0:-1]

    def __str__(self):
        return (
            f" Имя: {self.name} \n Фамилия: {self.surname} \n"
            f" Средняя оценка за домашние задания: {round(self.average_rating_student(), 2)} \n"
            f" Курсы в процессе изучения: {self.print_list(self.courses_in_progress)} \n"
            f" Завершенные курсы:{self.print_list(self.finished_courses)} \n"
            f" ___________________________________________________________"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
        return self.average_rating_student() < other.average_rating_student()


def all_student_by_cource(student_list, cource):
    all_gr = []
    for stud in student_list:
        if cource in stud.grades:
            for each_grade in stud.grades[cource]:
                all_gr.append(each_grade)
    return round((sum(all_gr) / len(all_gr)), 2)


def all_lector_by_cource(lector_list, cource):
    all_lec = []
    for lec in lector_list:
        if cource in lec.lector_grades:
            for each_grade in lec.lector_grades[cource]:
                all_lec.append(each_grade)
    return round((sum(all_lec) / len(all_lec)), 2)


# Иницмавализация студентов
s1 = Student('Иван', 'Иванов')
s1.courses_in_progress.append('SQL')
s1.finished_courses.append('BD')
s2 = Student('Петр', 'Петров')
s2.courses_in_progress.append('BD')
s2.courses_in_progress.append('SQL')
s2.finished_courses.append('Python')

# Иницмавализация проверяющих
r1 = Reviewers('Василий', 'Энштейн')
r1.attach_courses('SQL')
r1.attach_courses('BD')
r1.attach_courses('Python')
r2 = Reviewers('Капец', 'Капица')
r2.attach_courses('BD')

# Иницмавализация читающих
l1 = Lectors('Екатерина', 'Великая')
l1.attach_courses('BD')
l1.attach_courses('SQL')
l2 = Lectors('Просто', 'Вася')
l2.attach_courses('SQL')

# Выставление оценок
s1.rate_lector(l1, 'BD', 8)
s1.rate_lector(l1, 'Python', 9)
s2.rate_lector(l1, 'BD', 8)
s2.rate_lector(l1, 'SQL', 9)
s2.rate_lector(l1, 'BD', 2)
s1.rate_lector(l2, 'BD', 8)
s1.rate_lector(l2, 'Python', 9)
s2.rate_lector(l2, 'BD', 5)
s2.rate_lector(l2, 'SQL', 2)
r1.rate_student(s1, 'BD', 8)
r2.rate_student(s1, 'BD', 7)
r1.rate_student(s1, 'SQL', 4)
r1.rate_student(s2, 'BD', 9)
r1.rate_student(s2, 'BD', 2)
r1.rate_student(s1, 'BD', 4)
r1.rate_student(s1, 'BD', 1)

# перегрузка STR
print(s1)
print(s2)
print(r1)
print(r2)
print(l1)
print(l2)
# перегрузка BOOL
print(s1 > s2)
print(l1 < l2)

list_students = [s1, s2]
print(str(all_student_by_cource(list_students, 'SQL')))

list_lector = [l1, l2]
print(str(all_lector_by_cource(list_lector, 'BD')))

# For testing
print("Оценки s1 ", s1.grades)
print("Оценки s2 ", s2.grades)
print('Актиивные курсы студента s1', s1.courses_in_progress)
print('Завершенные курсы студента s1', s2.finished_courses)
print('Актиивные курсы студента s2', s2.courses_in_progress)
print('Завершенные курсы студента s2', s2.finished_courses)
print("Оценки l1 ", l1.lector_grades)
print("Оценки l2 ", l2.lector_grades)
print('Курсы проверяющего r1', r1.courses_attached)
print('Курсы проверяющего r2', r2.courses_attached)
