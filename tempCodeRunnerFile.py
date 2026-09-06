from backend.database import getCarsFromDatabase
from logic.carLogic import getValidIntInput, searchCars, sortCars

def main():

    carsOnMarket = getCarsFromDatabase()

    print("\nWelcome to Car Marketplace Search!")

    userRequestedCar = input("What car brand are you looking for? (e.g. Toyota, Ford, Tesla, BMW): ")
    userMaxPrice = getValidIntInput("What is your maximum price? ")
    userMaxMileage = getValidIntInput("What is your maximum mileage? ")
    
    matchingCars = searchCars(userRequestedCar, userMaxPrice, userMaxMileage, carsOnMarket)

    if len(matchingCars) == 0:
        print("Sorry, we couldn't find any cars that match your criteria.")
    else:
        print("Sort results by:")
        print("1. Price (lowest to highest)")
        print("2. Mileage (lowest to highest)")
        print("3. Year (oldest to newest)")
        print("4. Original order (unsorted)")

        userSortingChoice = getValidIntInput("Enter the number corresponding to your choice: ")
        while userSortingChoice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid option.")
            userSortingChoice = getValidIntInput("Enter the number corresponding to your choice: ")

        sortedCars = sortCars(matchingCars, userSortingChoice)
        for car in sortedCars:
            print(f"{car['year']} {car['make']} {car['model']} - ${car['price']} - {car['mileage']} miles")

if __name__ == "__main__":
    main()