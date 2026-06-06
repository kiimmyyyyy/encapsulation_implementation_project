import time

class Car:
    def __init__(self, year_model: str, make:str) -> None:
        self.__year_model: str = year_model
        self.__make: str = make
        self.__speed: float = 0.0

    def speed(self) -> float:
        return self.__speed
    def accelerate(self) -> None:
        self.__speed += 5
    def brake(self) -> None:
        self.__speed = max(0, self.__speed - 5)

def run_telemetry_sim(car: Car, action: str, iterations: int = 5) -> None:
    print(f"\n Initializing Telemetry: {action.upper()} Phase")
    print("=" *45)

    