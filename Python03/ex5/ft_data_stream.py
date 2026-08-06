from typing import Generator
import random


def gen_event(names: list[str],
              actions: list[str]) -> Generator[tuple[str, str]]:
    name = random.choice(names)
    action = random.choice(actions)
    yield (name, action)


def consume_event(players_list: list[tuple[str, str]]) -> Generator[tuple[str, str]]:
    while players_list:
        index_to_delete = random.randrange(len(players_list))
        yield players_list.pop(index_to_delete)


def main() -> None:
    players_names = ["alice", "bob", "charlie", "dylan"]
    players_actions = ["climb", "eat", "grab", "move",
                       "release", "run", "sleep", "swim",
                       "use"]
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        name, action = next(gen_event(players_names, players_actions))
        print(f"Event {i}: Player {name} did action {action}")
    players_list = []
    for i in range(10):
        players_list.append(next(gen_event(players_names, players_actions)))
    print(f"Built list of 10 events: {players_list}")
    for event in consume_event(players_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {players_list}")


if __name__ == "__main__":
    main()
