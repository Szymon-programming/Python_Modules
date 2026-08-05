import sys
from typing import IO


def main():
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    name_of_file = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accesing file '{name_of_file}'")
    try:
        file_stream = open(name_of_file, "r")
    except FileNotFoundError as e:
        print(f"Error opening file '{name_of_file}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{name_of_file}': {e}")
        return
    except IsADirectoryError:
        print("it's a directory you can't read from it")
        return
    data = file_stream.read()
    print("---")
    print()
    print(data)
    print()
    print("---")
    file_stream.close()
    print(f"File {name_of_file} closed.")



if __name__ == "__main__":
    main()