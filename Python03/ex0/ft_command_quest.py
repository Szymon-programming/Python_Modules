import sys

argument_count = len(sys.argv)
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if argument_count == 1:
	print("No arguments provided!")
else:
	i = 1
	print(f"Arguments received: {argument_count - 1}")
	for argument in sys.argv[1:]:
		print(f"Argument {i}: {argument}")
		i += 1
print(f"total arguments: {argument_count}")
print()