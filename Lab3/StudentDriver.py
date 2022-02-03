from Student import *

if __name__ == '__main__':
    student1 = Student(id=123456, firstName="Johnnie", lastName="Smith")
    student1.addCourse("CSE-101", 3.50)
    student1.addCourse("CSE-102", 3.00)
    student1.addCourse("CSE-201", 4.00)
    student1.addCourse("CSE-220", 3.75)
    student1.addCourse("CSE-325", 4.00)

    student2 = Student(id=234567, firstName="Jamie", lastName="Strauss")
    student2.addCourse("CSE-101", 3.00)
    student2.addCourse("CSE-103", 3.50)
    student2.addCourse("CSE-202", 3.25)
    student2.addCourse("CSE-220", 4.00)
    student2.addCourse("CSE-401", 4.00)

    student3 = Student(id=345678, firstName="Jack", lastName="O'Neill")
    student3.addCourse("CSE-101", 2.50)
    student3.addCourse("CSE-102", 3.50)
    student3.addCourse("CSE-103", 3.00)
    student3.addCourse("CSE-104", 4.00)

    student4 = Student(id=456789, firstName="Susie", lastName="Marks")
    student4.addCourses({'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00})

    student5 = Student(id=567890, firstName="Frank", lastName="Marks")
    student5.addCourses({'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00})

    student6 = Student(id=654321, firstName="Annie", lastName="Marks")
    student6.addCourses({'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00})

    student7 = Student(456987, "John", "Smith", {'CSE-101': 2.50, 'CSE-103': 3.00, 'CSE-210': 3.50, 'CSE-260': 4.00})
    student8 = Student(456987, "Judy", "Smith",
                       {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00})
    student9 = Student(111354, "Kelly", "Williams",
                       {'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50})
    student10 = Student(995511, "Brad", "Williams",
                        {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00})

    students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]
    Student.printStudents(students)

    # Query 1
    print("\nSort the list by lastName, firstName, both in ascending order")
    students.sort(key=lambda student: student.firstName)
    students.sort(key=lambda student: student.lastName)
    Student.printStudents(students)

    # Query 2
    print("\nSort the list by GPA in descending order")
    students.sort(key=lambda student: student.gpa)
    Student.printStudents(students)

    # Query 3
    print("\nunique courses taken by all students")
    all_courses = [list(student.courses.keys()) for student in students]
    set_of_unique_courses = set([item for sublist in all_courses for item in sublist])
    print(set_of_unique_courses)

    # Query 4
    print("\nGet a list of students who have taken ‘CSE-201’")
    students_in_CSE201 = [student for student in students if 'CSE-201' in student.courses.keys()]
    print(f"There are {len(students_in_CSE201)} students in CSE-201")
    Student.printStudents(students_in_CSE201)

    # Query 5
    print("\nGet a list of “honor roll” students (GPA >= 3.5)")
    honor_roll_students = [student for student in students if student.gpa >= 3.5]
    print(f"There are {len(honor_roll_students)} honor roll students")

    Student.printStudents(honor_roll_students)
