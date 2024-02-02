from Apartment import Apartment

class DailyRentalApartment(Apartment):

    def __init__(self, apartmentID, numberOFRooms, price, size, decorationStyle):
        Apartment.__init__(self, apartmentID, numberOFRooms, price, size)
        styles = ["Minimalist", "Modern", "Classic"]
        enumObj = enumerate(styles)
        for key,value in enumObj:
            if decorationStyle == key:
                self.decorationStyle = styles[decorationStyle]

    def calculateRentalPrice(self, numberOfDays):
            return self.price * numberOfDays

    def printInfo(self):
        Apartment.printInfo(self)
        print("Decoration Style: {}".format(self.decorationStyle),end="\n\n")



