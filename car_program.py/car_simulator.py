import time

class Car:
    """Encapsulated Vehicle"""
    def __init__(self, year_model: str, make:str) -> None:
        self.__year_model: str = year_model
        self.__make: str = make
        self.__speed: int = 0

    @property
    def speed(self) -> int:
        """Speed of the car"""
        return self.__speed

    def accelerate(self) -> None:
        """Vehicle acceleration by 5 units"""
        self.__speed += 5

    def brake(self) -> None:
        """Vehicle braking preventing negatives"""
        self.__speed = max(0, self.__speed - 5)

def run_telemetry_sim(car: Car, action: str, iterations: int = 5) -> None:
    print(f"\n Initializing Telemetry: {action.upper()} Phase")
    print("=" *45)

    for i in range(1, iterations + 1):
        time.sleep(0.2) #for delay hehe
        getattr(car, action.lower())()
        bar = "❚" * (car.speed // 2)
        print(f"Cycle {i} | Speed: {car.speed:02d} mph | {bar}")

def main() -> None:
    beast = Car(year_model="2026", make="CyberTruck")
    print(f"System Boot.. Tracking 2026 {beast._Car__make} status.")

    run_telemetry_sim(beast, action="accelerate")
    run_telemetry_sim(beast, action="brake")

    print("\n Simulation completed!")

if __name__ == "__main__":
    main()