import random


def main() -> None:
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                    'Gregory', 'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {initial_list}")
    capitalized_names = [x.capitalize() for x in initial_list]
    print(f"New list with all names capitalized: {capitalized_names}")
    capitalized_list = [x for x in initial_list if x == x.capitalize()]
    print(f"new list of capitalized names only: {capitalized_list}")
    print()
    score_dict = {name: random.randint(5, 1000) for name in capitalized_names}
    print(f"Score dict: {score_dict}")
    score_sum = sum([score_dict[name] for name in score_dict])
    avarage_score = round(score_sum / len(score_dict), 2)
    print(f"Score average is {avarage_score}")
    hight_scores = {name: score_dict[name] for name in score_dict
                    if score_dict[name] > avarage_score}
    print(f"High scores: {hight_scores}")


if __name__ == "__main__":
    main()
