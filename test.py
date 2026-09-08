# 1. Ask the user for a command
command = input("Enter a command (heater on / heater off): ")

# 2. Check what they typed
if command == "heater on":
    print("Turning the heater ON!")
elif command == "heater off":
    print("Turning the heater OFF!")
else:
    print("Unknown command!")

command2 = input("Enter a command: ")

pointer = command2.split()

if len(pointer) == 2:
    if pointer[0] == "point":
        satellite["pointing"] = pointer[1]
        print(f"Setting pointing angle to {number}!")
    else:
        print("Unknown action!")
else:
        print("You didint print anything")

