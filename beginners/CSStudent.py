from Student import Student


class CSStudent(Student):
    def __init__(self, name, major, gpa, is_on_probation, programming_language):
        super().__init__(name, major, gpa, is_on_probation)
        self.programming_language = programming_language

        def on_honor_roll(self):
            if self.gpa >= 3.5 and self.programming_language == "Python":
                return True
            else:
                return False
