import time

# ==========================================
# 1. INITIALIZATION (Set up starting state)
# ==========================================
satellite = {
    "battery": 100.0,
    "temp": 20.0,
    "heater_on": False,
    "pointing": 0
}

# ==========================================
# 2. THE SIMULATION LOOP (10 Ticks)
# ==========================================
for tick in range(10):

    # ------------------------------------------
    # STEP A: Operator Command Input & Parsing
    # ------------------------------------------
    command = input("Enter a command: ")
    pointer = command.split()

    if len(pointer) == 2:
        # Check index [0] for the command action
        if pointer[0] == "point":
            # Grab the angle at index [1]
            satellite["pointing"] = int(pointer[1])
            print(f"Setting pointing angle to {satellite['pointing']}!")

        # Check index [0] for the command action
        elif pointer[0] == "heater":
            # Grab the setting ("on" or "off") at index [1]
            setting = pointer[1]
            if setting == "on":
                satellite["heater_on"] = True
                print("Heater turned ON!")

            elif setting == "off":
                satellite["heater_on"] = False
                print("Heater turned OFF!")
            else:
                print("Invalid heater setting! Use 'on' or 'off'.")

        else:
            print("Unknown command! Use 'point <angle>' or 'heater <on/off>'.")

    else:
        # pressing Enter to let time pass!
        print("You didn't type anything")

    # ------------------------------------------
    # STEP B: Spacecraft Physics (Update temp & battery)
    # ------------------------------------------
    if satellite["heater_on"] == True:
        satellite["temp"] += 1.5
        satellite["battery"] -= 0.5
    else:
        satellite["temp"] -= 0.5
        satellite["battery"] -= 0.1

    # ------------------------------------------
    # STEP C: Safety Check (Critical Boundaries)
    # ------------------------------------------
    if satellite["battery"] <= 0:
        print("ALERT: BATTERY DEPLETED! Satellite is shutting down.")
        break

    # ------------------------------------------
    # STEP D: Telemetry Output & Simulation Pause
    # ------------------------------------------
    print(f"Tick {tick}: battery = {satellite['battery']:.1f}%, temp = {satellite['temp']:.1f}°C")
    time.sleep(1)