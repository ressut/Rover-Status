import math
#Start Progam
#Input
angle_degrees = float(input("Enter the Angle between 0 and 90:"))
if (angle_degrees > 90) or (angle_degrees < 0):
    print("The angle value must be between 0 and 90:")
time = float(input("Enter the time of the travel:"))
#Converting Angle
angle_radians = math.radians(angle_degrees)
#Constants
battery_total = 100
battery_usage = 0.027
speed = 1.5
travel_parameters = 0-90
#Calculation
cos = math.cos(angle_radians)
sin = math.sin(angle_radians)
distance = speed*time
battery_consumed = battery_usage*time
battery_ramaining = battery_total-battery_consumed
horizontal = distance*math.cos(angle_radians)
vertical = distance*math.sin(angle_radians)

#Output
print(f"Angle: {angle_degrees} Time: {time}")
print(f"Distance Travelled: {distance}")
print(f"Horizontal Movement: {horizontal:.2f}")
print(f"Vertical Movement: {vertical:.2f}")
print(f"Battery Usage: {battery_consumed:.2f}")
print(f"Battery Remaining: {battery_ramaining}")
