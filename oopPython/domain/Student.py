from domain.User import User


class Student(User):

    program = None

    def __init__(self, id_user, name, mail, password, program):
        super.__init__(id_user, name, mail, password)
        self._program = program

    @property
    def program(self):
        return self._program


    @program.setter
    def program(self, program):
        self._program = program

    def create_user(self):
        super().create_user()
        program = input("programa")
        self.students[self.id_user] = self.name, self.mail, self.password, self._program

     def list_users(self):
        for i in self.user.items():
            print(i)


