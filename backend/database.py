import sqlite3

def getCarsFromDatabase():
    
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    c.execute("SELECT id, make, model, year, price, mileage FROM cars")
    rows = c.fetchall()

    c.close()
    conn.close()
    
    cars = []

    for row in rows:
        car = {
            "id": row[0],
            "make": row[1],
            "model": row[2],
            "year": row[3],
            "price": row[4],
            "mileage": row[5]
        }
        cars.append(car)

    return cars

def addCar(make, model, year, price, mileage):
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    c.execute("INSERT INTO cars (make, model, year, price, mileage) VALUES (?, ?, ?, ?, ?)",
              (make, model, year, price, mileage))

    conn.commit()
    c.close()
    conn.close()

def deleteCar(carId):
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    
    c.execute("DELETE FROM cars WHERE id = ?", (carId,))

    conn.commit()
    c.close()
    conn.close()

def updateCar(carId, newPrice, newMileage):
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    c.execute("UPDATE cars SET price = ?, mileage = ? WHERE id = ?",
              (newPrice, newMileage, carId))

    conn.commit()
    c.close()
    conn.close()

def carExists(carId):
    cars = getCarsFromDatabase()

    for car in cars:
        if car["id"] == carId:
            return True
        
    return False