def main():
    carsOnMarket = [{
                        "make": "Toyota",
                        "model": "Camry",
                        "year": 2020,
                        "price": 18000,
                        "mileage": 60000
                    },

                    {
                        "make": "Toyota",
                        "model": "Supra",
                        "year": 2023,
                        "price": 29500,
                        "mileage": 18500
                    },

                    {
                        "make": "Ford",
                        "model": "Focus",
                        "year": 2015,
                        "price": 7200,
                        "mileage": 115000
                    },

                    {
                        "make": "Tesla",
                        "model": "Model 3",
                        "year": 2021,
                        "price": 31000,
                        "mileage": 42000
                    },

                    {
                        "make": "BMW",
                        "model": "M340i",
                        "year": 2024,
                        "price": 54000,
                        "mileage": 15000
                    }]


    print("Welcome to Car Marketplace Search!")

    userRequestedCar = input("What car brand are you looking for? (e.g. Toyota, Ford, Tesla, BMW): ")
    userMaxPrice = get_valid_int_input("What is your maximum price? ")
    userMaxMileage = get_valid_int_input("What is your maximum mileage? ")
    

    matchingCars = searchCars(userRequestedCar, userMaxPrice, userMaxMileage, carsOnMarket)

    if len(matchingCars) == 0:
        print("Sorry, we couldn't find any cars that match your criteria.")
    else:
        for car in matchingCars:
            print(f"{car['year']} {car['make']} {car['model']} - ${car['price']} - {car['mileage']} miles")

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