from car import Car

def main():
    my_car = Car("Toyota", "Camry", 2022)
    print(f"My car is a {my_car.get_descriptive_name()}.")

    my_car.read_odometer()

if __name__ == "__main__":
    main()
