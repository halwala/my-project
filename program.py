from car import Car

def main():
    my_car = Car("Honda", "Accord", 2021)
    print(f"My car is a {my_car.get_descriptive_name()}.")

    my_car.read_odometer()  # Initially 0 miles

    drive_car(my_car, 25)
    my_car.read_odometer()  # Now shows 25 miles

    try:
        my_car.update_odometer(10)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

