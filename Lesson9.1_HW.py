class Student:
    def __init__(self, name='Ivan', group='10A', age=18):
        self.name = name
        self.group = group
        self.age = age

    def get_name(self):
        print(f"Name - {self.name}")

    def get_age(self):
        print(f'Age - {self.age}')

    def get_group(self):
        print(f'Group - {self.group}')

    def new_name_age(self):
        new_name = input('Enter new name: ')
        new_age = input('Enter new age: ')
        self.name = new_name
        self.age = new_age

    def new_group(self):
        new_group = input('Enter new group number: ')
        self.group = new_group


student1 = Student()
student1.get_name()
student1.get_age()
student1.get_group()
student1.new_name_age()
student1.get_name()
student1.get_age()
student1.new_group()
student1.get_group()
print()

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'Addition of {self.a} and {self.b} = {self.a + self.b}')

    def multiplication(self):
        print(f'Multiplication of {self.a} and {self.b} = {self.a * self.b}')

    def division(self):
        print(f'Division of {self.a} and {self.b} = {self.a / self.b}')

    def subtraction(self):
        print(f'Subtraction of {self.a} and {self.b} = {self.a - self.b}')


exercise = Math(20, 5)
exercise.addition()
exercise.multiplication()
exercise.subtraction()
exercise.division()
print()

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def run(self):
        print('Car is launch')

    def drown_out(self):
        print('Car is drown out')

    def change_color(self):
        new_color = input('Enter new car\'s color: ')
        self.color = new_color

    def change_year(self):
        new_year = input('Enter new car\'s year: ')
        self.year = new_year

    def change_type(self):
        new_type = input('Enter new car\'s type: ')
        self.type = new_type

    def printed(self):
        print(f'Model - {self.type}\n'
              f'Color - {self.color}\n'
              f'Year - {self.year}')


gentra = Car('White', 'Chevrolet', '2009')
gentra.run()
gentra.drown_out()
gentra.change_type()
gentra.change_color()
gentra.change_year()
gentra.printed()


