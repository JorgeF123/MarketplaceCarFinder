from backend.database import addCar, deleteCar, updateCar, getCarsFromDatabase, carExists
from logic.carLogic import getValidIntInput

print("\nAdmin Menu")
print("1. Add car")
print("2. Update car")
print("3. Delete car")
print("4. View all cars")
print("5. Exit")
print("NOTE: When updating or deleting a car, you will need to provide the car's ID, which can be found by viewing all cars in the database (option 4).")

adminChoice = getValidIntInput("Enter your choice (1-5): ")
while adminChoice not in [1, 2, 3, 4, 5]:
    print("Invalid choice. Please select a valid option.")
    adminChoice = getValidIntInput("Enter your choice (1-5): ")

if adminChoice == 1:

    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = getValidIntInput("Enter car year: ")
    price = getValidIntInput("Enter car price: ")
    mileage = getValidIntInput("Enter car mileage: ")

    addCar(make, model, year, price, mileage)
    print(f"{year} {make} {model} added to the database.")

elif adminChoice == 2:
    carId = getValidIntInput("Enter the ID of the car you want to update: ")

    if carExists(carId) == False:
        print(f"No car found with ID {carId}.")
    else:
        newPrice = getValidIntInput("Enter new price: ")
        newMileage = getValidIntInput("Enter new mileage: ")

        updateCar(carId, newPrice, newMileage)
        print(f"Car with ID {carId} updated.")

elif adminChoice == 3:
    carId = getValidIntInput("Enter the ID of the car you want to delete: ")

    if carExists(carId) == False:
        print(f"No car found with ID {carId}.")
    else:
        deleteCar(carId)
        print(f"Car with ID {carId} deleted from the database.")

elif adminChoice == 4:
    cars = getCarsFromDatabase()

    if len(cars) == 0:
        print("No cars in the database.")
    else:
        for car in cars:
            print(f"ID: {car['id']} - {car['year']} {car['make']} {car['model']} - ${car['price']} - {car['mileage']} miles")

elif adminChoice == 5:
    print("Exiting admin menu.")   
