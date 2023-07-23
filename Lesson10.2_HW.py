class Vehicles:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f'Brand - {self.brand}\n'
              f'Year - {self.year}\n')


class Motorcycle(Vehicles):
    def __init__(self, brand, year, spaciousness):
        super().__init__(brand, year)
        self.spaciousness = spaciousness

    def display_info(self):
        print(f'Brand - {self.brand}\n'
              f'Year - {self.year}\n'
              f'Spaciousness - {self.spaciousness}\n')


class Car(Vehicles):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        print(f'Brand - {self.brand}\n'
              f'Year - {self.year}\n'
              f'Color - {self.color}\n')


tractor = Vehicles('Lamborghini', 2018)
tractor.display_info()
motorcycle1 = Motorcycle('Honda', 2020, 1)
motorcycle1.display_info()
car1 = Car('Chevrolet', 2010, 'White')
car1.display_info()








