import sys
import time

class Pet:
    """REPRESENTING A SECURE PET PROFILE"""

    def __init__(self) -> None:
        self.__name: str = "UNINTIALIZED"
        self.__animal_type: str = "UNKNOWN"
        self.__age: int = 0

    def set_name(self, name: str) -> None:
        self.__name = name.strip().title() if name.strip() else "Unknown Subject"

    def set_animal_type(self, animal_type: str) -> None:
        match animal_type.strip().lower():
            case "cat" | "kitten" | "feline":
                self.__animal_type = "Felis catus (Cat)"
            case "hamster" | "rodent":
                self.__animal_type = "Cricetinae (Hamster)"
            case "fish" | "goldfish" | "blobfish":
                self.__animal_type = "Actinopterygii (Fish"
            case "dog" | "bulldog" | "shih tzu":
                self.__animal_type = "Canis lupus familiaris (Dog)"
            case _:
                self.__animal_type = animal_type.strip().capitalize()

    def set_age(self, age:int) -> None:
        self.__age = max(0, age)

    def get_name(self) -> str:
        return self.__name

    def get_animal_type(self) -> str:
        return self.__animal_type

    def get_age(self) -> int:
        return self.__age

def matrix_print(text: str, speed: float = 0.015) -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_loading_bar() -> None:
    matrix_print("Injecting Data Encapsulated Core...")
    for i in range(1, 21):
        time.sleep(0.04)
        progress = "❚" * i + "❚" * (20 - i)
        sys.stdout.write(f"\r [{progress}] {i*5}% Secure")
        sys.stdout.flush()
    print("\n\n ENCRYPTION COMPLETED!")

def main() -> None:
    print("   _______________________________     ")
    print("  |          PET CORE 2.0         |    ")
    print("  |_______________:)______________|    ")

    subject = Pet()

    try:
        name_in = input("Enter the name of the pet -,- ")
        type_in = input("Enter the type of pet -,- ")
        age_in = int(input("Enter the age of the pet  -,- "))

        print()
        show_loading_bar()

        subject.set_name(name_in)
        subject.set_animal_type(type_in)
        subject.set_age(age_in)

    except ValueError:
        print("\n CRITICAL ERROR: Invalid Data Type. Agent Terminated!")
        sys.exit()

    matrix_print("======== DATABANK PROFILE OVERRIDE ========")
    matrix_print(f"MEMORY LOC: {hex(id(subject)).upper()}")
    matrix_print(f"TARGET NAME: {subject.get_name()}")
    matrix_print(f"CLASSIFICATION: {subject.get_animal_type()}")
    matrix_print(f"LIFESPAN INDEX: {subject.get_age()} cycles")
    matrix_print("==============___________==================")

if __name__ == "__main__":
    main()
