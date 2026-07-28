def ft_garden_intro(name: str, height: int, age: int) -> None:
	print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days")

def main() -> None:
    name = "Rose"
    height = 15
    age = 30
        
    print("=== Welcome to My Garden ===")
    ft_garden_intro(name, height, age)
    print("\n=== End of Program ===")  

if __name__ == "__main__":
    main()