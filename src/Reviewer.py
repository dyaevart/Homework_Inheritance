from Student import Student
from Mentor import Mentor


class Reviewer(Mentor):
    """
    Класс, который описывает ревьюера домашних заданий
    Оценки студентам может выставлять только ревьюер
    """
    def __init__(self, name, surname):
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
        return "Имя: {reviewer.name}\nФамилия: {reviewer.surname}".format(reviewer=self)