from car import Car


if __name__ == "__main__":
    print("hola mundo")
    car = Car()
    car.licence = "AMS234"
    car.driver = "Ricardo Sanchez"
    print(vars(car))

    car2 = Car()
    car2.licence = "QW255"
    car2.driver = "Moises Reyes"
    print(vars(car2))
