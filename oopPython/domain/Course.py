

class Course:

    _id_course = None
    _course_name = None
    _teacher = None

    def __init__(self, id_course, course_name, teacher ):
        self._id_course = id_course
        self._course_name = course_name
        self._teacher = teacher

    # getters and setters

    @property
    def id_course(self):
        return self.id_course

    @id_course.setter
    def id_course(self, id_course):
        self.id_course = id_course

    @property
    def course_name(self):
        return self.course_name

    @course_name.setter
    def course_name(self, course_name):
        self.course_name = course_name

    @property
    def teacher(self):
        return self.teacher

    @teacher.setter
    def teacher(self, teacher):
        self.teacher = teacher

    courses = {}

    def create_courses(self, teacher):
        self._id_course = int(input("Identificacion curso"))
        self._course_name = input("Nombre Curso")
        id_teacher = int(input("Ingrese el id del profe"))
        self._teacher = teacher.user[id_teacher]
        self.courses[self._id_course] = self._course_name, self.

    def list_courses(self):
        for i in self.courses.items():
            print(i)
