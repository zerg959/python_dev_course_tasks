class Contact:
    def __init__(self, name, phone, birthday):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def show(self):
        print(f'Name:{self.name}, Phone:{self.phone}, Birthday:{self.birthday}')

    def __str__(self):
        return f'Contact:{self.name}'

ivan = Contact('Ivan', '777', '13/01/1982')
print(ivan)