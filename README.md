# Marketplace Car Finder

Marketplace Car Finder is a small Python project for searching used cars based on simple filters.

## V0.5

Changes from V0.4:

* Moved the sample car data out of `main.py`
* Added a `cars.json` file
* Added JSON loading with `json.load()`
* The program now reads car data from `cars.json`

Current features:

* Stores sample car data in `cars.json`
* Lets the user search by make, maximum price, and maximum mileage
* Uses a `searchCars()` function to find matching cars
* Uses a `get_valid_int_input()` function for number validation
* Uses a `sortCars()` function to sort results
* Displays matching cars

## Run the Program

```bash
python3 main.py
```

## Future Plans

Future versions may include:

* Database support
* REST API
* Real car listing data
* Deal scoring

## Built With

* Python
* JSON
