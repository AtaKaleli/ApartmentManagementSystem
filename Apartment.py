class Apartment:

    __slots__ = ["apartmentID", "numberOFRooms", "price", "size"]

    def __init__(self, apartmentID, numberOFRooms, price, size):

        self.apartmentID = apartmentID
        self.numberOFRooms = numberOFRooms
        self.price = price
        self.size = size

    def getApartmentID(self):
        return self.apartmentID

    def getNumberOFRooms(self):
        return self.numberOFRooms

    def getPrice(self):
        return self.price

    def getSize(self):
        return self.size

    def setApartmentID(self, apartmentID):
        self.apartmentID = apartmentID

    def setNumberOFRooms(self, numberOFRooms):
        self.numberOFRooms

    def setPrice(self, price):
        self.price = price

    def setSize(self, size):
        self.size = size

    def printInfo(self):
        print("ApartmentID: {}".format(self.apartmentID))
        print("Number of Rooms: {}".format(self.numberOFRooms))
        print("Price: {}".format(self.price))
        print("Size: {}".format(self.size))








