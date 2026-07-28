class Plant:
	def __init__(self, name: str, height: float, age_var: int):
		self.name = name
		self.height = height
		self.age_var = age_var

	def show(self):
		print(f"Create: {self.name}: {self.height}cm, {self.age_var} days old")

	def grow(self):
		self.height = round(self.height + 0.8, 2)

	def age(self):
		self.age_var += 1

def main():
	plant1 = Plant("Rose", 25.0, 30)
	plant2 = Plant("Sunflowe", 80.0, 45)
	plant3 = Plant("Cactus", 15.0, 120)
	plant4 = Plant("Oak", 200.0, 365)
	plant5 = Plant("Fern", 15.0, 120)
	print("=== Plant Factory Output ===")
	plant1.show()
	plant2.show()
	plant3.show()
	plant4.show()
	plant5.show()
	

if __name__ == "__main__":
	main()