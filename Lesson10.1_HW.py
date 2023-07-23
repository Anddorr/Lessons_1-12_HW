class Animals:
    def make_sound(self, sound):
        print(sound)


class Dog(Animals):
    def make_sound(self):
        print('woof woof')


class Cat(Animals):
    def make_sound(self):
        print('moore moore')


class Cow(Animals):
    def make_sound(self):
        print('mu mu')


animal1 = Animals()
animal1.make_sound('la la')
dog1 = Dog()
dog1.make_sound()
cat1 = Cat()
cat1.make_sound()
cow1 = Cow()
cow1.make_sound()

1