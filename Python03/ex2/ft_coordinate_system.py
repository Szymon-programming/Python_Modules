import math

def get_player_pos():
	try:
		x, y, z = int(input("Enter new coordinates as floats in format 'x,y,z' : "))
		cords = (x,y,z)
		return cords
	except:
		