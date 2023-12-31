class A:
    def a(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(B):
    def a(self):
        print('C')

class D(C, A):
    def a(self):
        super(B, self).a()

D() .a()


class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('Weak password')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n')