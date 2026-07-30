class Plant:

    def __init__(self, name: str, height: float, age_var: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_var = 0
        self.set_height(height)
        self.set_age(age_var)

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


class Flower(Plant):

    def __init__(self, name: str, height: float,
                 age_var: int, color: str) -> None:
        super().__init__(name, height, age_var)
        self.color = color
        self.isblooming = False

    def bloom(self) -> None:
        self.isblooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.isblooming == True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name: str, height: float,
                 age_var: int, trunk_diameter: float):
        super().__init__(name, height, age_var)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float,
                 age_var: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age_var)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow_and_age(self, days: int) -> None:
        self.age_var += days
        self.height += round(2.1*days, 2)
        self.nutritional_value = days
        self.show()


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.grow_and_age(20)


if __name__ == "__main__":
    main()

