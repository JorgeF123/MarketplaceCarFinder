import json

def main():

    with open("cars.json", "r") as file:
        carsOnMarket = json.load(file)

    print("Welcome to Car Marketplace Search!")

    userRequestedCar = input("What car brand are you looking for? (e.g. Toyota, Ford, Tesla, BMW): ")
    userMaxPrice = get_valid_int_input("What is your maximum price? ")
    userMaxMileage = get_valid_int_input("What is your maximum mileage? ")
    

    matchingCars = searchCars(userRequestedCar, userMaxPrice, userMaxMileage, carsOnMarket)

    if len(matchingCars) == 0:
        print("Sorry, we couldn't find any cars that match your criteria.")
    else:
        print("Sort results by:")
        print("1. Price (lowest to highest)")
        print("2. Mileage (lowest to highest)")
        print("3. Year (oldest to newest)")
        print("4. Original order (unsorted)")

        userSortingChoice = get_valid_int_input("Enter the number corresponding to your choice: ")
        while userSortingChoice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid option.")
            userSortingChoice = get_valid_int_input("Enter the number corresponding to your choice: ")

        sortedCars = sortCars(matchingCars, userSortingChoice)
        for car in sortedCars:
            print(f"{car['year']} {car['make']} {car['model']} - ${car['price']} - {car['mileage']} miles")
            
       
def sortCars(cars, sortChoice):

    if sortChoice == 1:
        return sorted(cars, key=lambda car: car["price"])
    elif sortChoice == 2:
        return sorted(cars, key=lambda car: car["mileage"])
    elif sortChoice == 3:
        return sorted(cars, key=lambda car: car["year"])
    elif sortChoice == 4:
        return cars
    

def get_valid_int_input(prompt_message):

    while True:
        userInput = input(prompt_message)
        try:
            userInput = int(userInput)
            if userInput <= 0:
                print("Please enter a positive number.")
                continue
            return userInput
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def searchCars(make, maxPrice, maxMileage, cars):

    matchingCars = []

    for car in cars:

        if ((car["make"].lower() == make.lower())
            and (car["price"] <= maxPrice) 
            and (car["mileage"] <= maxMileage)
        ):
            matchingCars.append(car)

    return matchingCars
                

if __name__ == "__main__":
    main()