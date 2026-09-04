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

userRequestedCar = input("What car brand are you looking for? ")
userMaxPrice = int(input("What is your maximum price? "))
userMaxMileage = int(input("What is your maximum mileage? "))

for car in carsOnMarket:
    if (car["make"].lower() == userRequestedCar.lower() ) and (car["price"] <= userMaxPrice) and (car["mileage"] <= userMaxMileage):
        print(f"We have a {car['year']} {car['make']} {car['model']} for ${car['price']} with {car['mileage']} miles.")
        