import sqlite3

conn = sqlite3.connect('cars.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS cars
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  make TEXT,
                  model TEXT,
                  year INTEGER,
                  price REAL,
                  mileage INTEGER)''')

def insert_car(make, model, year, price, mileage):
    c.execute('''INSERT INTO cars (make, model, year, price, mileage)
                 VALUES (?, ?, ?, ?, ?)''', (make, model, year, price, mileage))
    conn.commit()

create_table()


insert_car("Toyota", "Camry", 2020, 18000, 60000)
insert_car("Toyota", "Supra", 2023, 29500, 18500)
insert_car("Ford", "Focus", 2015, 7200, 115000)
insert_car("Tesla", "Model 3", 2021, 31000, 42000)
insert_car("BMW", "M340i", 2024, 54000, 15000)

c.close()
conn.close()
