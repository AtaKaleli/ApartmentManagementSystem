from Building import Building

class Agency:

    def __init__(self, name):
        self.name = name
        self.buildings = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getBuildings(self):
        return self.buildings

    def addBuilding(self, building):
        self.buildings.append(building)

    def printBuildingsWithAddreses(self):
        for building in self.buildings:
            building.printBuildingWithAddress()

    def printApartmentWithRoom(self, numberOfRooms):
        for building in self.buildings:
            for apartment in building.getApartments():
                if apartment.numberOFRooms == numberOfRooms:
                    apartment.printInfo()

    def printApartmentWithBiggerSize(self, size):
        for building in self.buildings:
            for apartment in building.getApartments():
                if apartment.size > size:
                    apartment.printInfo()

    def printApartmentWithCheaperPrice(self, price, numberOfDays):
        for building in self.buildings:
            for apartment in building.getApartments():
                if apartment.calculateRentalPrice(numberOfDays) < price:
                    apartment.printInfo()

    def printApartmentBasedOnType(self):
        monthlyApartmentList = []
        dailyApartmentList = []
        for building in self.buildings:
            for apartment in building.getApartments():
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
            for building in self.buildings:
                for apartment in building.getApartments():
                    if apartment.apartmentID == apartmentID:
                        return apartment.calculateRentalPrice(numberOfDays)