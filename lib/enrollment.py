from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []


    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()


    # Student Class Aggregate Methods
    def course_count(self):
        """counts the number of courses a Student is a part of"""
        return len(self._enrollments)

    #Now lets assume the Student has a grades attribute. This attribute can be a dictionary where the key is the enrollment and the value is the grade. 
    #Lets write a method that would give us the average grade for a student across all the courses they are enrolled in.

    def aggregate_average_grade(self):
        # lets assume the grades are stored in a protected attribute called _grades. 
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses

        return average_grade

        # Since in this example we don't care about the course and only the grades lets get the values from the grades dictionary
        #  using self._grades.values(). We can now sum the grades and divide
        #  it by the number of the courses we have which will end up being the average of the students grades across all the enrollments.

class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    # Enrollment class Aggregate method
    @classmethod
    def aggregate_enrollments_per_day(cls):
        """how many enrollments were done for any day students were enrolled"""
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
