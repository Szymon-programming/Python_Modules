def garden_operations(operation_number):
	print(f"Testing operation {operation_number}")
	if operation_number == 0:
		return int('abc')
	elif operation_number == 1:
		return 5/0
	elif operation_number == 2:
		return open("text")
	elif operation_number == 3:
		return "22" + 2
	else:
		return  
			

def test_error_types():
	for i in [0, 1, 2, 3, 4]:
		try:
			garden_operations(i)
			print("Operation completed successfully")
		except ValueError as ex:
			print(f"Caught ValueError: {ex}")
		except ZeroDivisionError as ex:
			print(f"Caught ValueError: {ex}")
		except FileNotFoundError as ex:
			print(f"Caught ValueError: {ex}")
		except TypeError as ex:
			print(f"Caught ValueError: {ex}")


def main():
	print("=== Garden Error Types Demo ===")
	test_error_types()
	print()
	print("All error types tested successfully")


if __name__ == "__main__":
	main()