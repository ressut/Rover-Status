import math
#Start Progam
#Input
angle_degrees = float(input("Enter the Angle between 0 and 90:"))
if (angle_degrees > 90) or (angle_degrees < 0):
    print("The angle value must be between 0 and 90:")
    exit()
battery_total = 100
battery_usage = 0.027
time_to_die = battery_total/battery_usage
time = float(input("Enter the time of the travel:"))
if (time >= time_to_die):
    print("The Rover Battery will need to be Re-charded after reaching the final destination")
    exit()
#Converting Angle
angle_radians = math.radians(angle_degrees)
#Constants
speed = 1.5
#Calculation
distance = speed*time
battery_consumed = battery_usage*time
battery_remaining = battery_total-battery_consumed
horizontal = distance*math.sin(angle_radians)
vertical = distance*math.cos(angle_radians)
#Output
print(f"Angle: {angle_degrees} Time: {time}")
print(f"Distance Travelled: {distance}")
print(f"Horizontal Movement: {horizontal:.2f}")
print(f"Vertical Movement: {vertical:.2f}")
print(f"Battery Usage: {battery_consumed:.2f}")
print(f"Battery Remaining: {battery_remaining:.2f}")
if (battery_remaining <= 10):
    print(f"Battery Remaining is low")

