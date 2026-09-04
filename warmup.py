import time

# 1. This is a dictionary storing the satellite's state
satellite = {
    "battery": 100.0,
    "temp": 20.0,
    "heater_on": False
}

# 2. This loop will run 10 times (10 ticks)
for tick in range(10):
    # 3. subtract 0.5 from the battery each tick so it changes
    # 1. Temperature: +1.5°C per tick if heater is ON; -0.5°C if OFF.
    if satellite["heater_on"] == True:
        satellite["temp"] += 1.5
        satellite["battery"] -= 0.5 # heavy drain when heater is on
    else:
        satellite["temp"] -= 0.5
        satellite["battery"] -= 0.1 # light drain when heater is off

    # 4. Print the tick number and the current state
    print(f"Tick {tick}: battery = {satellite['battery']:.1f}%, temp = {satellite['temp']:.1f}°C")

    # 5. Pause the program for 1 second before looping again
    time.sleep(1)

# should see 10 lines print out, one second at a time, showing the battery dropping from 100.0 down to 95.0

# 2. Battery: -0.1% per tick naturally; -0.5% per tick if heater is ON.
