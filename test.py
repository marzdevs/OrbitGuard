# 1. Ask the user for a command
command = input("Enter a command (on/off): ")

# 2. Check what they typed
if command == "on":
    print("Turning the heater ON!")
elif command == "off":
    print("Turning the heater OFF!")
else:
    print("Unknown command!")