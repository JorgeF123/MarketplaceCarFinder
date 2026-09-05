import sqlite3

def main():

   
    carsOnMarket = getCarsFromDatabase()

    print("Welcome to Car Marketplace Search!")

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
            
def getCarsFromDatabase():
    
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    c.execute("SELECT make, model, year, price, mileage FROM cars")
    rows = c.fetchall()

    c.close()
    conn.close()
    
    cars = []

    for row in rows:
        car = {
            "make": row[0],
            "model": row[1],
            "year": row[2],
            "price": row[3],
            "mileage": row[4]
        }
        cars.append(car)

    return cars

def sortCars(cars, sortChoice):

    if sortChoice == 1:
        return sorted(cars, key=lambda car: car["price"])
    elif sortChoice == 2:
        return sorted(cars, key=lambda car: car["mileage"])
    elif sortChoice == 3:
        return sorted(cars, key=lambda car: car["year"])
    elif sortChoice == 4:
        return cars
    

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
                

if __name__ == "__main__":
    main()