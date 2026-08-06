import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for argument in sys.argv[1:]:
        try:
			if ":" in argument:
				item, quantity = argument.split(":", 1)
			else:
				raise SyntaxError
			if item in inventory:
				raise KeyError
			inventory[item] = int(quantity)
		except KeyError:
			print(f"Redundant item '{item}' - discarding")
		except ValueError as e:
			print(f"Quantity error for 'key': {e}")
		except SyntaxError:
			print(f"Error - invalid parameter '{argument}'")
    print(f"got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    inventor_size = len(item_list)
    inventory_quantity = sum(inventory.values())
    if inventor_size > 1:
        print(f"Total quantity of the {inventor_size}"
              f" items: {inventory_quantity}")
    else:
        print(f"Total quantity of the {inventor_size}"
              f" item: {inventory_quantity}")
    for item in inventory:
        item_quantity = round((inventory[item] / inventory_quantity) * 100, 1)
        print(f"Item {item} represents {item_quantity}%")
    most_abundant = max(inventory, key=lambda quantity: inventory[quantity])
    print(f"Item most abundant: {most_abundant} with"
          f" quantity {inventory[most_abundant]}")
    least_abundant = min(inventory, key=lambda quantity: inventory[quantity])
    print(f"Item least abundant: {least_abundant} with"
          f" quantity {inventory[least_abundant]}")
    inventory.update(magic_item=1)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
