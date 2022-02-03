from Lab3.Student import Student

def test_add_course():
    student = Student(id=1, firstName="Fred", lastName="Flintstone")
    student.addCourse("cse-100", 4)
    student.addCourse("cse-101", 2)
    student.addCourse("cse-102", 3)
    gpa = student.gpa()
    assert gpa == 3.0

    student1 = Student(id=2, firstName="Barney", lastName="Rubble")
    student1.addCourse("cse-100", 1)
    student1.addCourse("cse-101", 2)
    student1.addCourse("cse-102", 3)

    # print(repr(student))
    print()
    print(student)
    print(student1)
