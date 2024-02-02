from Apartment import Apartment
from DailyRentalApartment import DailyRentalApartment
from MonthlyRentalApartment import MonthlyRentalApartment
from Building import Building
from Agency import  Agency

def commandLineInterface():
    print("!!!Welcome to Agency Management System!!!")
    print("---------------------------------------------")
    print("Please select an operation")
    print("1. Add a new building to the agency")
    print("2. Add a new apartment (monthly or daily rental) to a building")
    print("3. List all buildings with their addresses")
    print("4. List all apartments available for the agency")
    print("5. List all apartments that have the specified number of rooms")
    print("6. List all apartments which are bigger than the specified apartment size")
    print("7. List all apartments which are cheaper than the specified price in a specified number of days")
    print("8. List all apartments that are either daily or monthly rental")
    print("9. Calculate the price of a specific apartment in a specified number of days")
    print("9. Calculate the price of a specific apartment in a specified number of days")



def menu():
    agency = Agency("METU NCC")
    commandLineInterface()
    while True:

        buildingCount = 0
        apartmentCount = 0

        agencyList = []
        buildingList = []
        apartmentList = []

        print("---------------------------------------------")
        option = int(input("Your selection: "))

        if option == 1:
            address = input("What is the address of your building: ")
            building = Building(buildingCount, address)
            agency.addBuilding(building)
            print("The building is created with id number {}".format(buildingCount))
            buildingCount += 1

        elif option == 2:
            print("Which building you want to add apartment into?")
            agency.printBuildingsWithAddreses()
            buildingID = int(input("Building ID: "))
            print("What is the type of the apartment? ")
            print("1. Daily Rental Apartment")
            print("2. Monthly Rental Apartment")
            type = int(input("Enter your choice: "))
            apartmentID = apartmentCount
            numberOfRooms = int(input("Enter number of rooms: "))
            rent = int(input("Enter rent (GBP): "))
            size = int(input("Enter size (m2): "))
            if type == 1:
                print("Decoration Style:")
                print("Minimalist")
                print("Modern")
                print("Classic")
                decorationStyle = input("Your Selection: ")
                apartment = DailyRentalApartment(apartmentID, numberOfRooms, rent, size, decorationStyle)


            elif type == 2:
                furnished = int(input("Furnished (yes(1)/no(0)): "))
                apartment = MonthlyRentalApartment(apartmentID, numberOfRooms, rent, size, furnished)

            for building in agency.getBuildings():
                if building.buildingID == buildingID:
                    building.addApartment(apartment)
            apartmentCount += 1
            print("Apartment successfully added")

        elif option == 3:
            agency.printBuildingsWithAddreses()

        elif option == 4:
            agency.printApartmentBasedOnType()

        elif option == 5:
            numberOfRooms = int(input("Enter the specified room number: "))
            agency.printApartmentWithRoom(numberOfRooms)

        elif option == 6:
            minimumSize = int(input("Enter minimum size: "))
            agency.printApartmentWithBiggerSize(minimumSize)

        elif option == 7:
            price = int(input("Enter the price(GBP): "))
            days = int(input("Enter the number of days: "))
            agency.printApartmentWithCheaperPrice(price, days)

        elif option == 8:
            rentalChoice = int(input("Enter Daily or Monthly Rental(0/1): "))
        #   complete

        elif option == 9:
            agency.printBuildingsWithAddreses()
            buildingId = int(input("Select building ID: "))
        #   complete

        elif option == 0:
            print("Thanks for choosing Agency Management System!")
            exit()
        else:
            print("Please Enter option between 0-9! ")






if __name__ == "__main__":
    menu()









