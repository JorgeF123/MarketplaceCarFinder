# Marketplace Car Finder

Marketplace Car Finder is a small Python project for searching used cars based on simple filters.

## V0.6

Changes from V0.5:

* Added SQLite database support
* Added a `cars.db` database
* Added a database setup file to create the `cars` table and insert sample cars
* Replaced JSON loading in `main.py` with database loading
* Added a `getCarsFromDatabase()` function
* The program now reads car data from SQLite

Current features:

* Stores sample car data in `cars.db`
* Lets the user search by make, maximum price, and maximum mileage
* Uses a `searchCars()` function to find matching cars
* Uses a `getValidIntInput()` function for number validation
* Uses a `sortCars()` function to sort results
* Reads cars from the SQLite database
* Displays matching cars

## Run the Program

```bash
python3 main.py
```

## Future Plans

Future versions may include:

* Add, update, and delete cars from the database
* REST API
* Real car listing data
* Deal scoring

## Built With

* Python
* SQLite

## Previous Data Format

`cars.json` is kept in the project from V0.5, but V0.6 now uses `cars.db` as the main data source.
