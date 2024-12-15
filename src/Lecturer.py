from Mentor import Mentor


class Lecturer(Mentor):
    """
    Класс, который описывает лектора, ведущего курсы
    Студенты могут выставлять лектору оценки
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    @classmethod
    def get_all_average_grades(self, lecturer):
        flat_list = sum(list(lecturer.lecturer_grades.values()), [])
        return sum(flat_list) / len(flat_list)

    def __str__(self):
        flat_grades_list = sum(list(self.lecturer_grades.values()), [])
        return ("Имя: " + self.name + "\n" + "Фамилия: " + self.surname + "\n" +
                "Средняя оценка за лекции: " + str(sum(flat_grades_list) / len(flat_grades_list)))

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return Lecturer.get_all_average_grades(self) < Lecturer.get_all_average_grades(other)


    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return Lecturer.get_all_average_grades(self) > Lecturer.get_all_average_grades(other)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return Lecturer.get_all_average_grades(self) == Lecturer.get_all_average_grades(other)