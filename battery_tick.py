import time                    # let it pause 1 second import

sat = {"battery": 100.0, "temp": 20.0}   # starting values

for i in range(10):            # will be 0,1,2,...9
    sat["battery"] -= 0.5      # battery drops a little
    print(i, sat)              # show the numbers
    time.sleep(1)