class GardenError(Exception):
	def __init__(self, message: str = "Unknown plant error"):
		self.message = message
		super().__init__(message)

	def __str__(self):
		return f"Caught {self.__class__.__name__}: {self.message}"


class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error"):
		super().__init__(message)


class WaterError(GardenError):
	def __init__(self, message: str = "Unknown plant error"):
		super().__init__(message)

	
def check_plant(status: str):
	if status == "wilting":
		raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int):
	if water_level < 1000:
		raise WaterError("Not enough water in the tank!")


def main():
	print("=== Custom Garden Errors Demo ===")
	print()
	print("Testing PlantError...")
	for i in ["wilting", 900]:
		try:
			check_plant(i)
			print()
			print("Testing WaterError...")
			check_water(i)
		except PlantError as pe:
			print(pe)
		except WaterError as pe:
			print(pe)
	print()
	print("Testing catching all garden errors...")
	for i in ["wilting", 700]:
		try:
			check_plant(i)
			check_water(i)
		except GardenError as pe:
			print(f"Caught GardenError: {pe.message}")
	print()
	print("All custom error types work correctly!")


if __name__ == "__main__":
	main()