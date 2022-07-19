class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_marks = {}

    def lecture_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_list:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'error'

    def avg_hw_grade(self):
        all_grade = 0
        counter = 0
        for grade_list in self.courses_marks.values():
            for marks in grade_list:
                counter += 1
                all_grade += marks
        return round(all_grade / counter, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_hw_grade() < other.avg_hw_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_hw_grade()}\nКурсы в процессе изучения: {(", ").join(self.courses_in_progress)}\nЗавершённые курсы: {(", ").join(self.finished_courses)}'
        return res

    def append_done_course(self, course):
        self.finished_courses.append(course)
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_list = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_lecture_grade(self):
        all_lecture_grade = 0
        counter = 0
        for list_lec_grade in self.grades.values():
            for marks_lec in list_lec_grade:
                counter += 1
                all_lecture_grade += marks_lec
        return round(all_lecture_grade / counter, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.avg_lecture_grade() < other.avg_lecture_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_lecture_grade()}'
        return res


class Reviewer(Mentor):
    def marks_gets(self, student, course, mark):
        if isinstance(student, Student) and course in self.courses_list and course in student.courses_in_progress:
            if course in student.courses_marks:
                student.courses_marks[course] += [mark]
            else:
                student.courses_marks[course] = [mark]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res




student_1 = Student('Michael', 'Townley', 'man')
student_2 = Student('Franklin', 'Clinton', 'man')
lecturer_1 = Lecturer('Severus', 'Snape')
lecturer_2 = Lecturer('Rubeus', ' Hagrid')
reviewer_1 = Reviewer('Carl', 'Jonhson')
reviewer_2 = Reviewer('Trevor', 'Phillips')

student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('JavaScript')
student_1.finished_courses.append('Git')
student_1.finished_courses.append('C#')


student_2.courses_in_progress.append('Java')
student_2.courses_in_progress.append('Pascal')
student_2.courses_in_progress.append('JavaScript')
student_2.finished_courses.append('C++')

reviewer_1.courses_list.append('Java')
reviewer_1.courses_list.append('JavaScript')
reviewer_1.courses_list.append('Pascal')

reviewer_2.courses_list.append('Python')

lecturer_1.courses_list.append('Python')

lecturer_2.courses_list.append('Python')
lecturer_2.courses_list.append('Java')

reviewer_1.marks_gets(student_2, 'Java', 10)
reviewer_1.marks_gets(student_2, 'Java', 8)
reviewer_1.marks_gets(student_2, 'JavaScript', 10)
reviewer_1.marks_gets(student_1, 'JavaScript', 8)
reviewer_1.marks_gets(student_1, 'JavaScript', 7)
reviewer_2.marks_gets(student_1, 'Python', 10)
reviewer_2.marks_gets(student_1, 'Python', 9)
print(f'Оценки первого студента: {student_1.courses_marks}')
print(f'Оценки второго студента: {student_2.courses_marks}')
print()

student_1.lecture_grade(lecturer_1, 'Python', 10)
student_1.lecture_grade(lecturer_2, 'Python', 9)
student_2.lecture_grade(lecturer_2, 'Java', 10)
print(f'Оценки за лекции у первого лектора: {lecturer_1.grades}')
print(f'Оценки за лекции у второго лектора: {lecturer_2.grades}')
print()

print(reviewer_2)
print()
print(lecturer_2)
print()
print(student_1)
print()

print(lecturer_1 > lecturer_2)
print(lecturer_2 < lecturer_1)
print(student_2 < student_1)
print(student_2 > student_1)
print()


students_list = [student_1, student_2]


def avg_grade_students(study, course):
    all_students_grade = 0
    counter = 0
    for student in study:
        if course in student.courses_marks:
            for grade in student.courses_marks[course]:
                counter += 1
                all_students_grade += grade
        else:
            pass
    print(f'Средняя оценка за домашние задания на курсе по "{course}": {round(all_students_grade / counter, 2)}')


avg_grade_students(students_list, 'JavaScript')

lecture_list = [lecturer_1, lecturer_2]


def avg_grade_lecture(lecture, course):
    all_lecture_grades = 0
    counter = 0
    for lecturer in lecture:
        if course in lecturer.grades:
            for grades in lecturer.grades[course]:
                counter += 1
                all_lecture_grades += grades
        else:
            pass
    print(f'Средняя оценка за лекции по "{course}": {round(all_lecture_grades / counter, 2)}')


avg_grade_lecture(lecture_list, 'Python')



