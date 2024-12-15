from Lecturer import Lecturer


class Student:
    """
    Класс, который описывает студента, проходящего курсы
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    @classmethod
    def get_all_average_grades(self, student):
        flat_list = sum(list(student.grades.values()), [])
        return sum(flat_list) / len(flat_list)


    def __str__(self):
        return ("Имя: " + self.name + "\nФамилия: " + self.surname +
                "\nСредняя оценка за лекции: " + str(Student.get_all_average_grades(self)) +
                "\nКурсы в процессе изучения: " + ", ".join(map(str, self.courses_in_progress)) +
                "\nЗавершенные курсы: " + ", ".join(map(str, self.finished_courses)))

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return Student.get_all_average_grades(self) < Student.get_all_average_grades(other)


    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return Student.get_all_average_grades(self) > Student.get_all_average_grades(other)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return Student.get_all_average_grades(self) == Student.get_all_average_grades(other)