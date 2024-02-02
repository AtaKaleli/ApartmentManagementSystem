from Apartment import Apartment

class MonthlyRentalApartment(Apartment):

    def __init__(self, apartmentID, numberOFRooms, price, size, hasFurniture):
        Apartment.__init__(self, apartmentID, numberOFRooms, price, size)
        if hasFurniture == 1:
            self.hasFurniture = "Yes"
        else:
            self.hasFurniture = "No"

    def calculateRentalPrice(self, numberOfDays):
            return self.price * ((numberOfDays//30) + 1)

    def printInfo(self):
        Apartment.printInfo(self)
        print("hasFurniture: {}".format(self.hasFurniture),end="\n\n")




