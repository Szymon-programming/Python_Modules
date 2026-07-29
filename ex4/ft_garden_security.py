class Plant:

    def __init__(self, name: str, height: float, age_var: int) -> None:
        self.name = name
        self._height = None
        self.height = height
        self._age_var = None
        self.age_var = age_var
        print("Plant created: ", end="")
        print(f"{self.name}: {self.height}cm, {self.age_var} days old")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_var} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)

    def age(self) -> None:
        self.age_var += 1

    def get_age(self) -> None:
        return self._age_var

    def get_height(self) -> None:
        return self._height

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.age_var = value
            print(f"Age updated: {self.age_var} days")

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.height = value
            print(f"Height updated: {self.height}cm")


def main() -> None:
    # plant2 = Plant("Sunflower", 80.0, 45)
    # plant3 = Plant("Cactus", 15.0, 120)
    # plant4 = Plant("Oak", 200.0, 365)
    # plant5 = Plant("Fern", 15.0, 120)
    print("=== Garde Security System ===")
    plant1 = Plant("Rose", 25.0, 30)
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-6)
    plant1.set_age(-6)
    # plant2.show()
    # plant3.show()
    # plant4.show()
    # plant5.show()
    print("Current state: ", end="")
    plant1.show()


if __name__ == "__main__":
    main()
