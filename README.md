# Car Class Example

This repository contains a simple Python project that defines a `Car` class and demonstrates its usage. The project includes two files: `car.py` and `program.py`.

## Files

### `car.py`

This file defines the `Car` class with the following attributes and methods:

- Attributes:
  - `make`: The make of the car (e.g., Toyota, Honda).
  - `model`: The model of the car (e.g., Camry, Civic).
  - `year`: The year the car was manufactured.
  - `odometer_reading`: The current odometer reading of the car (default is 0).

- Methods:
  - `__init__(self, make, model, year)`: Initializes a new instance of the `Car` class with the given make, model, and year.
  - `get_descriptive_name(self)`: Returns a descriptive name of the car in the format "YEAR MAKE MODEL".
  - `read_odometer(self)`: Prints the current odometer reading of the car.
  - `update_odometer(self, mileage)`: Updates the odometer reading of the car to the given mileage, but only if the new mileage is greater than the current reading.
  - `increment_odometer(self, miles)`: Increments the odometer reading of the car by the given number of miles.

### `program.py`

This file demonstrates the usage of the `Car` class by creating instances of the class and calling its methods. It also includes a `drive_car` function that simulates driving a car for a given number of miles and updates the odometer reading accordingly.

## Usage

To run the project, you need to have Python installed on your system. Then, navigate to the project directory in your terminal or command prompt and run the `program.py` file:

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Additionally, you can open issues for bug reports or feature requests.

