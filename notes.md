# Assignment 1:
1. What happens to temperature when the heater is on vs. off
    - RULE: If the heater is on, the temperature rises by 1.5 degrees every tick. If the heater is off, the temperature falls by 0.5 degrees every tick.
    - is heater true or false in code and add or sub 
2. What happens to the battery each tick (heater costs extra energy)
   - every action consumes power and will cause battery to slowly drain over time and running heater drains it even faster.
   - RULE: The spacecraft battery naturally drains by 0.1% every tick. If the heater is active, it consumes extra energy, draining the battery by an additional 0.4% (for a total drop of 0.5% per tick).
   - CODE: with each loop sub amount from battery every second plus extra amount if heater set to true
3. What you do if the satellite battery hits 0%
    - RULE: If the battery level hits 0, the spacecraft goes completely dark. The program prints 'BATTERY DEPLETED - COLD OPERATIONAL FAILURE' and breaks out of the loop to terminate.
    - CODE: if satellite["battery"] <= 0

# ==========================================
# ORBITGUARD MISSION RULES (Assignment 1)
# 1. Temperature: +1.5°C per tick if heater is ON; -0.5°C if OFF.
# 2. Battery: -0.1% per tick naturally; -0.5% per tick if heater is ON.
# 3. Dead State: If battery hits 0, print failure message and stop loop.
# ==========================================