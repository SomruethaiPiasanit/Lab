from house import House
from apartment import Apartment
from rent import Rent
from purchase import Purchase


class HouseRental(House, Rent):
    pass


class HousePurchase(House, Purchase):
    pass


class ApartmentRental(Apartment, Rent):
    pass


class ApartmentPurchase(Apartment, Purchase):
    pass
