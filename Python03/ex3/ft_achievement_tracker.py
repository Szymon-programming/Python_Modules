import random


def gen_player_achievements(achievements):
	player_achievs = set(random.sample(achievements, 7))
	return player_achievs


def main():
	achievements_list = ['Crafting Genius', 'Strategist', 'World Savior',
							'Speed Runner', 'Survivor', 'Master Explorer',
							'Treasure Hunter', 'Unstoppable', 'First Steps',
							'Collector Supreme',
							'Untouchable', 'Sharp Mind', 'Boss Slayer']
	achiv_tuple = tuple(achievements_list)
	achiv_set = set(achievements_list)
	print("=== Achievement Tracker System ===")
	print()
	Alice_set = gen_player_achievements(achiv_tuple)
	Bob_set = gen_player_achievements(achiv_tuple)
	Charlie_set = gen_player_achievements(achiv_tuple)
	Dylan_set = gen_player_achievements(achiv_tuple)
	print(f"Player Alice: {Alice_set}")
	print(f"Player Bob: {Bob_set}")
	print(f"Player Charlie: {Charlie_set}")
	print(f"Player Dylan: {Dylan_set}")
	print()
	distinc_set = Alice_set.union(Bob_set, Charlie_set, Dylan_set)
	print(f"All distinct achievements: {distinc_set}")
	print()
	common_elem = Alice_set.intersection(Bob_set, Charlie_set, Dylan_set)
	print(f"Common achievements: {common_elem}")
	print()
	Alice_only = Alice_set - Bob_set.union(Charlie_set, Dylan_set)
	print(f"Only Alice has: {Alice_only}")
	Bob_only = Bob_set - Bob_set.union(Alice_set, Dylan_set)
	print(f"Only Bob has: {Bob_only}")
	Charlie_only = Charlie_set - Bob_set.union(Alice_set, Dylan_set)
	print(f"Only Charlie has: {Charlie_only}")
	Dylan_only = Dylan_set - Bob_set.union(Charlie_set, Alice_set)
	print(f"Only Dylan has: {Dylan_only}")
	print()
	Alice_missing = achiv_set.difference(Alice_set)
	print(f"Alice is missing: {Alice_missing}")
	Bob_missing = achiv_set.difference(Bob_set)
	print(f"Bob is missing: {Bob_missing}")
	Charlie_missing = achiv_set.difference(Charlie_set)
	print(f"Charlie is missing: {Charlie_missing}")
	Dylan_missing = achiv_set.difference(Dylan_set)
	print(f"Dylan is missing: {Dylan_missing}")


if __name__ == "__main__":
	main()

