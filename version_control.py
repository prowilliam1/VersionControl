#version 3
while True:
    name = input("Enter your name (or exit to quit): ")
    if name.lower() == "exit":
        break
    print(f"Hello, {name}")
