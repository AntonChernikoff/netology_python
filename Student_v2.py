def return_garde_avr_from_dct(grades:dict) -> float:
        grade_avr = 0
        grade_count = 0
        for course in grades:
            for grade in grades[course]:
                grade_avr += int(grade)
                grade_count += 1
        grade_avr = grade_avr/grade_count
        return grade_avr

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_for_lector(self, lecturer, course:str, grade:int):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка выставления оценки Лектору'

    def return_garde_avr(self) -> float:
        return return_garde_avr_from_dct(self.grades)

    def __str__(self) -> str:
        str_info = "===> Студент\n"
        str_info += f"Имя: {self.name}\n"
        str_info += f"Фамилия: {self.surname}\n"
        str_info += f"grades: {self.grades}\n"
        str_info += f"Средняя оценка за домашние задания: {self.return_garde_avr()}\n"
        str_info += f"Курсы в процессе изучения:{self.courses_in_progress}\n"
        str_info += f"Завершенные курсы::{self.finished_courses}"
        return str_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.return_garde_avr() < other.return_garde_avr()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка выставления оценки за ДЗ'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        print('Лектор не может выставлять оценку за ДЗ')

    def return_garde_avr(self):
        return return_garde_avr_from_dct(self.grades)

    def __str__(self) -> str:
        # grade_avr = 0
        # for grade in self.grades:
        #     grade_avr += grade_avr
        # grade_avr = grade_avr/len(self.grades)
        str_info = "===> Лектор\n"
        str_info += f"Имя: {self.name}\n"
        str_info += f"Фамилия: {self.surname}\n"
        # str_info += f"courses_attached: {self.courses_attached}\n"
        # str_info += f"grades: {self.grades}\n"
        # str_info += f"Средняя оценка за лекции: {grade_avr}"
        str_info += f"Средняя оценка за лекции: {self.return_garde_avr()}"
        return str_info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.return_garde_avr() < other.return_garde_avr()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) -> str:
        str_info = "===> Эксперт\n"
        str_info += f"Имя: {self.name}\n"
        str_info += f"Фамилия: {self.surname}"
        return str_info
        #return super().__str__()


student_1 = Student('Илья', 'Сергеевич', 'м')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']

student_2 = Student('Максим', 'Кирилович', 'м')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']

student_3 = Student('Денис', 'Максимович', 'м')
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Java']

student_4 = Student('Никита', 'Денисович', 'м')
student_4.courses_in_progress += ['C++']
student_4.courses_in_progress += ['Java']

lecturer_1 = Lecturer('Петр', 'Сергеевич')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Владимир', 'Борисович')
lecturer_2.courses_attached += ['C++']
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Антон', 'Владимирович')
lecturer_3.courses_attached += ['Python']

reviewer_1 = Reviewer('Артур','Николаевич')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Николай','Артурович')
reviewer_2.courses_attached += ['C++']

reviewer_3 = Reviewer('Олег','Сафронович')
reviewer_3.courses_attached += ['Java']

reviewer_1.rate_hw(student_1,'Python',7)
reviewer_1.rate_hw(student_2,'Python',8)
reviewer_1.rate_hw(student_3,'Python',9)
reviewer_1.rate_hw(student_4,'Python',10)
reviewer_2.rate_hw(student_1,'C++',10)
reviewer_2.rate_hw(student_2,'C++',9)
reviewer_2.rate_hw(student_4,'C++',10)

student_1.grade_for_lector(lecturer_1, 'Python', 8)
student_2.grade_for_lector(lecturer_3, 'Python', 9)
student_3.grade_for_lector(lecturer_3, 'Python', 9)
student_1.grade_for_lector(lecturer_2, 'C++', 10)
student_2.grade_for_lector(lecturer_2, 'C++', 9)
student_4.grade_for_lector(lecturer_2, 'C++', 10)

print("\n------- Students -------")
print(student_1)
print(student_2)
print(student_3)
print(student_4)
print("\n------- Lecturers -------")
print(lecturer_1)
print(lecturer_2)
print(lecturer_3)
print("\n------- Reviewers -------")
print(reviewer_1)
print(reviewer_2)
print(reviewer_3)
print("\n------- Сравнение -------")
print(f"Результат сравнения student_1 < student_2: {student_1 < student_2} student_1 = {student_1.return_garde_avr()} и student_2 = {student_2.return_garde_avr()}")
print(f"Результат сравнения lecturer_1 > lecturer_2: {lecturer_1 > lecturer_2} lecturer_1 = {lecturer_1.return_garde_avr()} и lecturer_2 = {lecturer_2.return_garde_avr()}")
