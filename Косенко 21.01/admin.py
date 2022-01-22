from user import User

class Privilegii():
    def __init__(self,privilegii):
        self.privilegii =privilegii
    def show_privilegii(self):
        print(f'Privilegii: {self.privilegii}')

class Admin(User, Privileges):
    def __init__(self, first_name, last_name, privilegii, login_attempts=0, ):
        super().__init__(first_name, last_name, login_attempts)
        self.privilegii = privilegii
