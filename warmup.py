import time

# 1. This is a dictionary storing the satellite's state
satellite = {"battery": 100.0, "temp": 20.0}

# 2. This loop will run 10 times (10 ticks)
for i in range(10):
    # 3. subtract 0.5 from the battery each tick so it changes
    satellite["battery"] -= 0.5

    # 4. Print the tick number and the current state
    print(i, satellite)

    # 5. Pause the program for 1 second before looping again
    time.sleep(1)

# should see 10 lines print out, one second at a time, showing the battery dropping from 100.0 down to 95.0