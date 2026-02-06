inventory = ["Apple","Bananas","Carrots"]
print("Current inventory:",inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final updated inventory:",inventory)

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
first_reading = temperatures[0]
last_reading = temperatures[-1]
afternoon_peak = temperatures[3:6]
last_3_hours = temperatures[-3:]
print("First Reading:", first_reading)
print("Last Reading:", last_reading)
print("Afternoon Peak Readings:", afternoon_peak)
print("Last 3 Hours Readings:", last_3_hours)

screen_res = (1920, 1080)
# Print current resolution
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
#  Fix: Explain immutability
print("Tuples cannot be modified!")