import time

# ==========================================
# 1. INITIALIZATION (Set up starting state)
# ==========================================
satellite = {
    "battery": 100.0,
    "temp": 20.0,
    "heater_on": False,
    "pointing": 0,
    "mode": "NOMINAL",
}


# ------------------------------------------
# STEP A: Operator Command Input & Parsing
# ------------------------------------------
def apply_command(command_message, satellite):
    pointer = command_message.lower().split()

    if len(pointer) == 2:
        # Check index [0] for the command action
        if pointer[0] == "point":

            # TASK 1: Check if in NOMINAL mode before updating pointing
            if satellite["mode"] == "NOMINAL":
                try:
                    satellite["pointing"] = int(pointer[1])
                    print(f"Setting pointing angle to {satellite['pointing']}!")
                except ValueError:
                    print("Invalid pointing angle! Please enter a valid number.")
            else:
                print("COMMAND REJECTED: Pointing disabled in SAFE mode!")

        # Check index [0] for the command action
        elif pointer[0] == "heater":
            # Grab the setting ("on" or "off") at index [1]
            setting = pointer[1]
            if setting == "on":
                if satellite["mode"] == "NOMINAL":
                    satellite["heater_on"] = True
                    print("Heater turned ON!")
                else:
                    print("COMMAND REJECTED: Heater cannot be turned ON in SAFE mode!")

            elif setting == "off":
                satellite["heater_on"] = False
                print("Heater turned OFF!")
            else:
                print("Invalid heater setting! Use 'on' or 'off'.")

        elif pointer[0] == "mode":
            setting = pointer[1]
            if setting == "safe":
                satellite["mode"] = "SAFE"
                print("WARNING: Satellite entering SAFE mode!")

            elif setting == "nominal":
                satellite["mode"] = "NOMINAL"
                print("Satellite returning to NOMINAL operations.")
            else:
                print("Invalid mode! Use 'safe' or 'nominal'.")
        else:
            print(
                "Unknown command! Use 'point <angle>', 'heater <on/off>', or 'mode safe/nominal'."
            )

    elif len(pointer) == 0:
        print("No command, time passes.")

    else:
        print("Invalid format! Commands are two words, ex: 'heater on'.")


# ------------------------------------------
# STEP B: Spacecraft Physics (Update temp & battery)
# ------------------------------------------
# TASK 2 (Option B): Physics Override keeps the heater off automatically in SAFE mode
def update_physics(satellite):

    if satellite["mode"] == "SAFE":
        satellite["heater_on"] = False

    if satellite["heater_on"] == True:
        satellite["temp"] += 1.5
        satellite["battery"] -= 0.5
    else:
        satellite["temp"] -= 0.5
        satellite["battery"] -= 0.1


# ------------------------------------------
# STEP D: Telemetry Output & Simulation Pause
# ------------------------------------------
def print_telemetry(satellite, tick):
    print(
        f"Tick {tick}: battery = {satellite['battery']:.1f}%, temp = {satellite['temp']:.1f}°C, heater_on = {satellite['heater_on']}, pointing = {satellite['pointing']}°, mode = {satellite['mode']}"
    )


for tick in range(10):
    # STEP A: Operator Command Input & Parsing
    command_message = input("Enter command (or press Enter to skip): ")
    apply_command(command_message, satellite)

    # STEP B: Spacecraft Physics (Update temp & battery)
    update_physics(satellite)

    # STEP C: Safety Check (Critical Boundaries)
    if satellite["battery"] <= 0:
        print("ALERT: BATTERY DEPLETED! Satellite is shutting down.")
        break

    # STEP D: Telemetry Output & Simulation Pause
    print_telemetry(satellite, tick)
    time.sleep(1)
