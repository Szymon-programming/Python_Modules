def input_temperature(temp_str: str):
	return int(temp_str)

def test_temperature():
	for i in ['25', 'abc']:
		try:
			print(f"Input data is '{i}'")
			input_temperature(i)
			print(f"temperature is now {i}C")
			print()
		except ValueError as ex:
			print(f"Caught input_temperature error: {ex}")

def main():
	print("=== Garden Temperature ===")
	test_temperature()
	print()
	print("All tests completed - program didn't crash!")


if __name__ == "__main__":
	main()