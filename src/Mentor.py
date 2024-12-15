class Mentor:
    """
    Класс, который описывает ментора, ведущего курсы
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
