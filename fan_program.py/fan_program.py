class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color='blue', on=False):
        self.__speed = speed
        self.__radius = float (radius)
        self.__color = str (color)
        self.__on = bool (on)

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            print("Invalid speed")

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = float(radius)
        else:
            print("Invalid radius")

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = str(color)

    def get_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = bool (on)

    def display_properties(self, name):
        print(f"{name} Properties ")
        print(f"Speed: {self.get_speed()}")
        print(f"Radius: {self.get_radius()}")
        print(f"Color: {self.get_color()}")
        print(f"On: {self.get_on()}")
        print("-" * 25)

def TestFan():
    fan1 = Fan()

    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10)
    fan1.set_color("yellow")
    fan1.set_on(True)

    fan2 = Fan()

    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5)
    fan2.set_color("blue")
    fan2.set_on(False)

    fan1.display_properties("Fan1")
    fan2.display_properties("Fan2")

if __name__ == "__main__":
    TestFan()

