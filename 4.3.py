class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"The {self.name} car has started.")

    def stop(self):
        print(f"The {self.name} car has stopped.")

    def turn(self, direction):
        print(f"The {self.name} car has turned {direction}.")

    def show_speed(self):
        print(f"The current speed of the {self.name} car is {self.speed} km/h.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Warning: Speed limit exceeded for a TownCar!")
        else:
            print(f"The current speed of the {self.name} car is {self.speed} km/h.")
        super().show_speed()

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Warning: Speed limit exceeded for a WorkCar!")
        else:
            print(f"The current speed of the {self.name} car is {self.speed} km/h.")
        super().show_speed()


class PoliceCar(Car):
    pass


try:
    car1 = TownCar(int(input("Enter the speed of the TownCar: ")), input("Enter the color of the TownCar: "),
               input("Enter the name of the TownCar: "), False)
except:
    print("Type Error!")
car1.go()
car1.show_speed()
car1.turn("left")
car1.stop()

try:
    car2 = WorkCar(int(input("Enter the speed of the WorkCar: ")), input("Enter the color of the WorkCar: "),
               input("Enter the name of the WorkCar: "), False)
except:
    print("Type Error!")
car2.go()
car2.show_speed()
car2.turn("right")
car2.stop()

try:
    car3 = SportCar(int(input("Enter the speed of the SportCar: ")), input("Enter the color of the SportCar: "),
                input("Enter the name of the SportCar: "), False)
except:
    print("Type Error!")
car3.go()
car3.show_speed()
car3.turn("straight")
car3.stop()

try:
    car4 = PoliceCar(int(input("Enter the speed of the PoliceCar: ")), input("Enter the color of the PoliceCar: "),
                 input("Enter the name of the PoliceCar: "), True)
except:
    print("Type Error!")
car4.go()
car4.show_speed()
car4.turn("around")
car4.stop()