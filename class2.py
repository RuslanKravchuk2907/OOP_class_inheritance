from class1 import Verification

class V2(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age


    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError ('This user is registered')
        super().save()

    def show(self):
        return self.login, self.password


x = V2('Nikolai','123456789','33')
