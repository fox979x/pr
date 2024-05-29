

class User:

    _id_user = None
    _name = None
    _mail = None
    _password = None

    def __init__(self, id_user, name, mail, password):
        self._id_user = id_user
        self._name = name
        self._mail = mail
        self._password = password

    @property
    def id_user(self):
        return self.id_user


    @id_user.setter
    def id_user(self, id_user):
        self.id_user = id_user


    @property
    def name(self):
        return self.name


    @name.setter
    def name(self, name):
        self.name = name


    @property
    def mail(self):
        return self.mail


    @mail.setter
    def mail(self, mail):
        self.mail = mail


    @property
    def password(self):
        return self.password


    @password.setter
    def password(self, password):
        self.password = password

    user = {}


    # metodos propios

    def create_user(self):
        self.id_user = input(input("Id"))
        self.name = input("Name")
        self.mail = input("Mail")
        self.password = input("Password")


