def getValidIntInput(prompt_message):

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


def sortCars(cars, sortChoice):

    if sortChoice == 1:
        return sorted(cars, key=lambda car: car["price"])
    elif sortChoice == 2:
        return sorted(cars, key=lambda car: car["mileage"])
    elif sortChoice == 3:
        return sorted(cars, key=lambda car: car["year"])
    elif sortChoice == 4:
        return cars