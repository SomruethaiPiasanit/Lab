from property import Property


class Apartment(Property):
    TT = 20

    def __init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry):
        Property().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        print(Property())
        print(self.balcony)
        print(self.laundry)

    @staticmethod
    def prompt_init(balcony, laundry):
        return{Property().prompt_init, "balcony": balcony, "laundry": laundry}


A1 = Apartment(10, 20, 30, 40, 40)
A1.display
