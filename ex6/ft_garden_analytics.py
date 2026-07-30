class Plant:

    class _StatData:

        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def increment_grow(self) -> None:
            self._grow += 1

        def increment_age(self) -> None:
            self._age += 1

        def increment_show(self) -> None:
            self._show += 1

        def display_statistics(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, {self._show} show")

    def __init__(self, name: str, height: float, age_var: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_var = 0
        self.set_height(height)
        self.set_age(age_var)
        self._stats = self._StatData()

    def show(self) -> None:
        self._stats.increment_show()
        print(f"{self.name}: {self.height}cm, {self.age_var} days old")

    def grow(self) -> None:
        self._stats.increment_grow()
        self.height = round(self.height + 0.8, 2)

    def age(self) -> None:
        self._stats.increment_age()
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

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.height = value

    def display_statistics(self) -> None:
            self._stats.display_statistics()

    @staticmethod
    def check_age(value: int) -> None:
        if value > 365:
            print(f"Is {value} days more than a year? -> True")
        elif value > 0:
            print(f"Is {value} days more than a year? -> False")
        else:
            print("invalid input")

    @classmethod
    def anonymo_plant(cls):
        return cls("Unknown", 0.0, 0)


class Flower(Plant):

    def __init__(self, name: str, height: float,
                 age_var: int, color: str) -> None:
        super().__init__(name, height, age_var)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming == True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name: str, height: float,
                 age_var: int, trunk_diameter: float):
        super().__init__(name, height, age_var)
        self.trunk_diameter = trunk_diameter
        self.shade_cals = 0

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self.shade_cals += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f" {self.shade_cals} shade")


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


class Seed(Flower):

    def __init__(self, name: str, height: float, age_var: int, color: str) -> None:
        super().__init__(name, height, age_var, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_any_stats(plant: Plant) -> None:
    plant.display_statistics()

def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_any_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_any_stats(rose)

    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_any_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_any_stats(oak)

    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_any_stats(sunflower)

    print()

    print("=== Anonymous")
    anonym = Plant.anonymo_plant()
    anonym.show()
    print("[statistics for Unknown plant]")
    display_any_stats(anonym)


if __name__ == "__main__":
    main()

