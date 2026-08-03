import sys

argv_count = len(sys.argv)
print("=== Player Score Analytics ===")
score = []
for argument in sys.argv[1:]:
	try:
		score.append(int(argument))
	except ValueError:
		print(f"Invalid parameter: '{argument}'")
score_count = len(score)
if score_count == 0:
	print("No scores Provided. ", end="")
	print(f"Usage: python3 {sys.argv[0]} <score1> <score2> ..." )
else:
	for argument in [score]:
		print(f"Scores processed: {argument}")
		print(f"Total players: {score_count}")
		print(f"Total score: {sum(score)}")
		print(f"Avarage score: {sum(score)/score_count}")
		print(f"High score: {max(score)}")
		print(f"Low score: {min(score)}")
		print(f"Score range: {max(score) - min(score)}")