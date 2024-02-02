from Apartment import Apartment
from DailyRentalApartment import DailyRentalApartment
from MonthlyRentalApartment import MonthlyRentalApartment

class Building:

    def __init__(self, buildingID, address):
        self.buildingID = buildingID
        self.address = address
        self.apartments = []

    def setBuildingID(self, buildingID):
        self.buildingID = buildingID

    def setAddress(self, address):
        self.address = address

    def getBuildingID(self):
        return self.buildingID

    def getAddress(self):
        return self.address

    def getApartments(self):
        return self.apartments

    def addApartment(self, apartment):
        self.apartments.append(apartment)

    def printApartmentWithRooms(self, numberOFRooms):
        for apartment in self.apartments:
            if apartment.numberOFRooms == numberOFRooms:
                apartment.printInfo()

    def printApartmentWithBiggerSize(self, size):
        for apartment in self.apartments:
            if apartment.size > size:
                apartment.printInfo()

    def printApartmentWithCheaperPrice(self, price, numberOfDays):
        for apartment in self.apartments:
            if apartment.calculateRentalPrice(numberOfDays) < price:
                apartment.printInfo()

    def printApartmentBasedOnType(self):

        monthlyApartmentList = []
        dailyApartmentList = []
        for apartment in self.apartments:
            # print(apartment.__class__)
            if apartment.__class__ == MonthlyRentalApartment:
                monthlyApartmentList.append(apartment)
            else:
                dailyApartmentList.append(apartment)

        print("MonthlyRentalApartments: ",end="\n\n")
        for apartment in monthlyApartmentList:
            apartment.printInfo()

        print("DailyRentalApartments: ", end="\n\n")
        for apartment in dailyApartmentList:
            apartment.printInfo()

    def calculateRentalPriceUsingID(self, apartmentID, numberOfDays):
        for apartment in self.apartments:
            if apartment.apartmentID == apartmentID:
                return apartment.calculateRentalPrice(numberOfDays)

    def printBuildingWithAddress(self):
        print("BuildingInfo: ",end="\n\n")
        print("ID: {} | Address: {}".format(self.buildingID, self.address))

    def printBuildingWithAllApartments(self):
        self.printBuildingWithAddress()
        for aparment in self.apartments:
            aparment.printInfo()


