import math

def get_player_pos():
	while True:
		try:
			cords = (input("Enter new coordinates as floats in format 'x,y,z': ")).split(',')
			if len(cords) < 3:
				raise SyntaxError
			i = 0
			while i < 3:
				try:
					cords[i] = float(cords[i])
				except ValueError as e:
					raise ValueError(f"'{cords[i]}': {e}")
				i = i + 1
			x = cords[0]
			y = cords[1]
			z = cords[2]
			cord = (x,y,z)
			return cord
		except ValueError as e:
			print(f"Error on parameter {e}")
		except SyntaxError:
			print("Invalid syntax")


def calculate_center_distance(cords1):
    x1, y1, z1 = cords1
    result = math.sqrt(x1**2 + y1**2 + z1**2)
    return round(result, 4)


def distance_between(cords1, cords2):
    x1, y1, z1 = cords1
    x2, y2, z2 = cords2
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(result, 4)

def main():
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    cords1 = get_player_pos()
    x1, y1, z1 = cords1
    print(f"Got a first tuple: {x1, y1, z1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    center_dist = calculate_center_distance(cords1)
    print(f"Distance to center: {center_dist}")
    print()
    print("Get a second set of coordinates")
    cords2 = get_player_pos()
    distance = distance_between(cords1, cords2)
    print(f"Distance between the 2 sets of coordinates: {distance}")

if __name__ == "__main__":
    main()
