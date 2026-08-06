def input_temperature(temp_str: str):
	temperature = int(temp_str)
	if temperature >= 0 and temperature <= 40:
		return temperature
	elif temperature > 40:
		raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
	else:
		raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

def test_temperature():
	for i in ['25', 'abc', '100', '-50']:
		try:
			print(f"Input data is '{i}'")
			input_temperature(i)
			print(f"temperature is now {i}°C")
			print()
		except ValueError as ex:
			print(f"Caught input_temperature error: {ex}")
			print()

def main():
	print("=== Garden Temperature Checker ===")
	print()
	test_temperature()
	print("All tests completed - program didn't crash!")


if __name__ == "__main__":
	main()