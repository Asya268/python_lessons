class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def get_index(self):
        return self.index

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def house(self):
        return self.house

    def get_apartment(self):
        return self.apartment
