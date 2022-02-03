import functools

class Student(object):
    def __init__(self, id, firstName, lastName, courses=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self._gpa = 0
        if courses is None:
            self.courses = dict()
        else:
            self.courses = courses

    def __str__(self):

        courses = ','.join([str(key) for key in self.courses.keys()])

        return f"{self.id:<12}{self.lastName:<12}{self.firstName:<12}{self.gpa:.3f} {courses}"

    def __repr__(self):
        return f"{self.id},{self.lastName},{self.firstName},{{{self.courses}}}"

    @classmethod
    def header(cls) -> str:
        header = f"{'ID':<12}{'Last Name':<12}{'First Name':<12}{'GPA':<12}{'Courses'}\n=========================================================================================="
        return header

    @property
    def gpa(self):
        """
        calculates the cumulative grade point average for the student based on courses
        :return: GPA or 0 if no courses
        """
        number_of_courses = len(self.courses)
        if number_of_courses is 0:
            return 0

        total_score = functools.reduce(lambda x, y: x + y, self.courses.values(), 0)
        average = total_score / number_of_courses
        return average

    def addCourse(self, course, score):
        assert isinstance(score, (int, float)), f"score {score} should be a number"
        assert score >= 0, f"score {score} should be greater that zero"
        assert score < 5, f"score {score} should be less than 5"
        self.courses.update({course: score})

    def addCourses(self, courses):
        assert isinstance(courses, dict), "Courses must be a dict"
        self.courses.update(courses)

    @classmethod
    def printStudents(cls, students):
        print(Student.header())
        for student in students:
            print(student)

