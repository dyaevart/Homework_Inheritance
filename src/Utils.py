class Utils:
    """
    Класс со вспомогательными методами
    """
    @classmethod
    def average_student_grades(cls, students, course_name):
        average_list=[]
        for student in students:
            for course, grade in student.grades.items():
                if course == course_name:
                    average_list += grade

        return str(sum(average_list) / len(average_list))

    @classmethod
    def average_lecturer_grades(cls, lecturers, course_name):
        average_list=[]
        for lecturer in lecturers:
            for course, grade in lecturer.lecturer_grades.items():
                if course == course_name:
                    average_list += grade

        return str(sum(average_list) / len(average_list))