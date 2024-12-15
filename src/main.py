from Student import Student
from Reviewer import Reviewer
from Mentor import Mentor
from Lecturer import Lecturer
from Utils import Utils

# создаём по 2 экземпляра каждого типа
student_1 = Student('Ruoy', 'Eman', 'male')
student_2 = Student('Helena', 'Lopez', 'female')
mentor_1 = Mentor('Anatoly', 'Anatoliev')
mentor_2 = Mentor('Sergey', 'Sergeev')
lecturer_1 = Lecturer('Olga','Olgina')
lecturer_2 = Lecturer('Alyona','Alenina')
reviewer_1 = Reviewer('Victor', 'Victorov')
reviewer_2 = Reviewer('Stepan','Stepanov')

# заполняем списки курсов у студентов и всех типов преподавателей
student_1.courses_in_progress += ['Python','Java']
student_2.courses_in_progress += ['Python', 'C++']
student_1.finished_courses += ['JavaScript','C#']
student_2.finished_courses += ['C#']
mentor_1.courses_attached += ['Python']
mentor_2.courses_attached += ['Java']
lecturer_1.courses_attached += ['Python', 'Java']
lecturer_2.courses_attached += ['Python', 'C++']
reviewer_1.courses_attached += ['Java']
reviewer_2.courses_attached += ['Python', 'Java', 'C++']

# выставляем оценки студентам и преподавателям
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'C++', 8)

student_1.rate_lecturer(lecturer_1,"Python", 4)
student_1.rate_lecturer(lecturer_1,"Python", 1)
student_1.rate_lecturer(lecturer_1,"Java", 10)
student_2.rate_lecturer(lecturer_1,"Python", 5)
student_2.rate_lecturer(lecturer_1,"Python", 6)

student_1.rate_lecturer(lecturer_2,"Python", 3)
student_2.rate_lecturer(lecturer_2,"Python", 7)

# вызываем переопределённый метод __str__
print(reviewer_1, end="\n\n")
print(reviewer_2, end="\n\n")
print(lecturer_1, end="\n\n")
print(lecturer_2, end="\n\n")
print(student_1, end="\n\n")
print(student_2, end="\n\n")

# вызываем переопределённые методы сравнения

if student_1 > student_2:
    print("У студента " + student_1.name + " средние оценки выше")
elif student_1 < student_2:
    print("У студента " + student_2.name + " средние оценки выше")
else:
    print("Средние оценки студентов равны")


if lecturer_1 > lecturer_2:
    print("У лектора " + lecturer_1.name + " средние оценки выше")
elif lecturer_1 < lecturer_2:
    print("У лектора " + lecturer_2.name + " средние оценки выше")
else:
    print("Средние оценки лекторов равны")


# вызываем специальные методы для подсчёта средних
print("Средние оценки по курсу: " + Utils.average_student_grades([student_1,student_2],"Python"))
print("Средние оценки по курсу: " + Utils.average_lecturer_grades([lecturer_1,lecturer_2],"Java"))




