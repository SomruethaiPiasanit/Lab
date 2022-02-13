class Property:
    def __init__(self, square_feet, num_bedrooms, num_bathrooms):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    def display(self):
        print(self.square_feet)
        print(self.num_bedrooms)
        print(self.num_bathrooms)

    @staticmethod
    def prompt_init(square_feet, num_bedrooms, num_bathrooms):
        return{"square_feet": square_feet, "num_bedrooms": num_bedrooms,
               ":num_bathrooms": num_bathrooms}
