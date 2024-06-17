import math
from datetime import datetime

date = datetime.now()
PI = math.pi
DIVIDER = 10000000000
CONSTANT = 2540

print(f"{date:%Y-%m-%d}")
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (PI * math.pow(width, 2) * aspect * (width * aspect + CONSTANT * diameter)) / DIVIDER

print(f"The approximate volume is {volume:.2f} liters")
user_answer = input("Do you want to buy tires with given dimentions(yes/no) ")
phone_number = "not contact"
if user_answer == "yes":
    phone_number = input("Write your phone number ten digits XXX-X-XX-XX-XX: ")
with open("volumes.txt", "at") as volumnes_file:
    print(date.strftime("%Y-%m-%d"), width, aspect, diameter, round(volume, 2),phone_number, file=volumnes_file)

