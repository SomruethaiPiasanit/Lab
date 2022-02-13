from property import Property


class House(Property):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard):
        Property().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        Property().display()

    def prompt_init():
        Property().prompt_init
