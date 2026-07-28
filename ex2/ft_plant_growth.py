class Plant:
	def __init__(self, name: str, height: float, age_var: int):
		self.name = name
		self.height = height
		self.age_var = age_var

	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age_var} days old")

	def grow(self):
		self.height = round(self.height + 0.8, 2)

	def age(self):
		self.age_var += 1

def main():
	plant1 = Plant("Rose", 25.0, 30)
	plant2 = Plant("Sunflowe", 80.0, 45)
	plant3 = Plant("Cactus", 15.0, 120)
	print("=== Garden Plant Growth ===")
	starting_height = plant1.height
	plant1.show()
	for i in range(7):
		print(f"=== Day {i+1} ===")
		plant1.grow()
		plant1.age()
		plant1.show()
	week_growth = round(plant1.height - starting_height, 2)
	print(f"Growth this week: {week_growth}")

if __name__ == "__main__":
	main()