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


def water_plant(plant_name: str):
	if plant_name == plant_name.capitalize():
		print(f"Watering {plant_name}", end="")
	else:
		raise PlantError(f"Invalid plant name to water {plant_name}")


def main():
	print("=== Garden Watering System ===")
	print()
	print("testing valid plants...")
	try: 
		print("Opening Watering System")
		for name in ["Tomato", "Lettuce", "Carrots"]:
			try:
				water_plant(name)
				print(" [OK]")
			except PlantError as ex:
				print(ex)
				print(".. ending tests and returning to main")
	finally:
		print("closing watering system")
	print()
	print("testing invalid plants...")
	try: 
		print("Opening Watering System")
		for name in ["Tomato", "lettuce", "Carrots"]:
			try:
				water_plant(name)
				print(" [OK]")
			except PlantError as ex:
				print(ex)
				print(".. ending tests and returning to main")
				break
	finally:
		print("closing watering system")
	print()
	print("Cleanup always happens, even with errors!")

			
			


if __name__ == "__main__":
	main()