# Marketplace Car Finder

Marketplace Car Finder is a Python project for searching and managing used car listings using an SQLite database.

## V0.7

Changes from V0.6:

* Added an admin menu
* Added the ability to add cars to the database
* Added the ability to update cars using their unique ID
* Added the ability to delete cars using their unique ID
* Added the ability to view all cars in the database
* Added a `carExists()` function to verify car IDs
* Reorganized the project into `backend` and `logic` folders
* Moved database-related files into the `backend` folder
* Moved car search and input logic into the `logic` folder

## Current Features

### User Features

* Search for cars by make
* Set a maximum price
* Set a maximum mileage
* Sort results by:
  * Price
  * Mileage
  * Year
  * Original order
* Display matching cars

### Admin Features

* Add a car
* Update a car
* Delete a car
* View all cars
* Uses unique car IDs for updating and deleting
* Checks if a car ID exists before updating or deleting

## Project Structure

```text
MarketplaceCarFinder/
│
├── backend/
│   ├── admin.py
│   ├── database.py
│   └── setupDatabase.py
│
├── logic/
│   └── carLogic.py
│
├── cars.db
├── cars.json
├── main.py
└── README.md