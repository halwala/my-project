from car import Car

def main():
    my_car = Car("Honda", "Accord", 2021)
    print(f"My car is a {my_car.get_descriptive_name()}.")

    my_car.read_odometer()

if __name__ == "__main__":
    main()

def drive_car(car, miles):
    print(f"Driving the {car.get_descriptive_name()} for {miles} miles.")
    car.increment_odometer(miles)

if __name__ == "__main__":
    main()
