from domain.User import User


class Teacher(User):

    _speciality = None

    def __init__(self, id_user, name, mail, password, speciality) :
        super().__init__(id_user, name, mail, password)
        self._speciality = speciality

    @property
    def speciality(self):
        return self._speciality


    @_speciality.setter
    def speciality(self, _speciality):
        self._speciality = _speciality



    def create_user(self):
        super().create_user()
        self._speciality = input("Especialidad")
        self.user[self.id_user] = self.name, self.mail, self.password, self._speciality

    def list_users(self):
        for i in self.user.items():
            print(i)