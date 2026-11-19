# OrbitGuard — Design Notes

## Satellite state

| Field     | Starts at | Meaning                                      |
| --------- | --------- | -------------------------------------------- |
| battery   | 100.0 %   | Power left                                   |
| temp      | 20.0 °C   | Spacecraft temperature                       |
| heater_on | False     | Heater on/off                                |
| pointing  | 0°        | Pointing angle in degrees (whole numbers)    |
| mode      | NOMINAL   | NOMINAL (normal ops) or SAFE (survival mode) |

---

## Assignment 1 — Onboard physics and heater

### 1. Temperature: heater on vs. off

- **RULE:** If the heater is on, the temperature rises by 1.5 °C every tick. If the heater is off, the temperature falls by 0.5 °C every tick.
- **CODE:** `update_physics()` checks whether `heater_on` is True or False and adds or subtracts from `temp`.

### 2. Battery drain each tick (the heater costs extra energy)

- Every action consumes power, so the battery slowly drains over time, and running the heater drains it even faster.
- **RULE:** The battery naturally drains by 0.1 % every tick. If the heater is on, it uses extra energy: an additional 0.4 %, for a total drop of 0.5 % per tick.
- **CODE:** Each tick, `update_physics()` subtracts 0.1 from `battery`, or 0.5 if the heater is on.

### 3. Battery hits 0 %

- **RULE:** If the battery reaches 0 % or below, the spacecraft goes completely dark. The program prints `ALERT: BATTERY DEPLETED! Satellite is shutting down.` and breaks out of the loop to end the simulation.
- **CODE:** `if satellite["battery"] <= 0:` in the main loop, then `break`.

---

## Assignment 2 — Operator commands (terminal)

Commands are typed while the simulation runs, so the source code never has to be edited to change the satellite. Commands are **two words** and **not case-sensitive** (`HEATER ON` works the same as `heater on`).

### Commands

| Command         | Effect                                                                         |
| --------------- | ------------------------------------------------------------------------------ |
| `heater on`     | Turns the heater on (NOMINAL only)                                             |
| `heater off`    | Turns the heater off (always allowed)                                          |
| `point <angle>` | Sets pointing to a whole number, e.g. `point 15` or `point -20` (NOMINAL only) |
| `mode safe`     | Enters SAFE mode                                                               |
| `mode nominal`  | Returns to NOMINAL mode                                                        |
| _(press Enter)_ | No command; time passes                                                        |

### Invalid input

| Input                                                          | Result                                                     |
| -------------------------------------------------------------- | ---------------------------------------------------------- |
| `point abc` (not a whole number)                               | Rejected with "Invalid pointing angle"; pointing unchanged |
| `heater maybe`                                                 | "Invalid heater setting"                                   |
| `mode sleep`                                                   | "Invalid mode"                                             |
| Unknown two-word command (e.g. `hello world`)                  | "Unknown command"                                          |
| One word, or three or more words (e.g. `hello`, `point 15 20`) | "Invalid format"                                           |

### SAFE mode rules

- Entering SAFE forces the heater **OFF**. This is checked every tick in `update_physics()`, so it takes effect the same tick SAFE is entered.
- `heater on` is **rejected** while in SAFE.
- `point <angle>` is **rejected** while in SAFE. The SAFE check happens _before_ the number check, so `point abc` in SAFE shows the SAFE rejection.
- `heater off` is still allowed.
- **Way back:** `mode nominal` returns the satellite to normal operations.

### Code structure (logic lives in functions)

| Function                                    | Job                                                                     |
| ------------------------------------------- | ----------------------------------------------------------------------- |
| `apply_command(command_message, satellite)` | Parses one operator command and changes the satellite state             |
| `update_physics(satellite)`                 | Updates temperature and battery for one tick; enforces SAFE heater rule |
| `print_telemetry(satellite, tick)`          | Prints battery, temp, heater, pointing and mode                         |

Main loop, each tick: read input → `apply_command` → `update_physics` → battery check → `print_telemetry` → sleep 1 second.

---

## Assignment 2 — Test results (Nov 19, 2026)

All tests passed.

| #   | Input                           | Expected                                           | Result |
| --- | ------------------------------- | -------------------------------------------------- | ------ |
| 1   | _(Enter)_                       | "No command, time passes"; temp −0.5, battery −0.1 | ✅     |
| 2   | `heater on`                     | Temp +1.5, battery −0.5                            | ✅     |
| 3   | `HEATER OFF`                    | Works (not case-sensitive)                         | ✅     |
| 4   | `point 15`                      | Pointing = 15°                                     | ✅     |
| 5   | `point -20`                     | Pointing = −20°                                    | ✅     |
| 6   | `point abc`                     | Rejected; pointing stays −20°                      | ✅     |
| 7   | `mode safe` (heater on)         | Heater forced off the same tick                    | ✅     |
| 8   | `heater on` in SAFE             | Rejected                                           | ✅     |
| 9   | `point 30` in SAFE              | Rejected; pointing unchanged                       | ✅     |
| 10  | `point abc` in SAFE             | SAFE rejection shown first                         | ✅     |
| 11  | `heater off` in SAFE            | Allowed                                            | ✅     |
| 12  | `mode nominal`, then `point 30` | Back to NOMINAL; pointing = 30°                    | ✅     |
| 13  | `hello`                         | "Invalid format"                                   | ✅     |
| 14  | `hello world`                   | "Unknown command"                                  | ✅     |
| 15  | `point 15 20`                   | "Invalid format"                                   | ✅     |
| 16  | `mode sleep`                    | "Invalid mode"                                     | ✅     |
| 17  | `heater maybe`                  | "Invalid heater setting"                           | ✅     |
| 18  | Battery 1.0 + `heater on`       | Shutdown alert; loop stops                         | ✅     |

---

## Open decisions / later

- Pointing has no range limit yet (e.g. 0–360). Decide later.
- Time only advances after a command, because `input()` waits for the operator.
- The simulation runs for 10 ticks (`range(10)`).
