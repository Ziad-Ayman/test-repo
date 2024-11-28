def greet(name):
    """
    Function to greet a person with their name.
    """
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
