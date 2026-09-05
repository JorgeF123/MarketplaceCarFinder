# Marketplace Car Finder

Marketplace Car Finder is a small Python project for searching used cars based on simple filters.

## V0.3

Changes from V0.2:

* Added a `get_valid_int_input()` function
* Added input validation for maximum price and maximum mileage
* Prevents negative number inputs
* Prevents invalid text input from crashing the program
* Added a message when no cars match the search criteria

Current features:

* Stores 5 sample cars
* Lets the user search by make, maximum price, and maximum mileage
* Uses a `searchCars()` function to find matching cars
* Displays matching cars

## Run the Program

```bash
python3 main.py
```

## Future Plans

Future versions may include:

* Better search and sorting
* JSON file storage
* Database support
* REST API
* Real car listing data
* Deal scoring

## Built With

* Python
