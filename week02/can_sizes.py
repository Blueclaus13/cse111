import math

def main():

    DATA = {
        "#1 Picnic": [6.83, 10.16],
        "#1 Tall": [7.78, 11.91],
        "#2": [8.73, 11.59],
        "#2.5": [10.32, 11.91],
        "#3 cylinder": [10.79, 17.78],
        "#5": [13.02, 14.29],
        "#6Z": [5.40, 8.89],
        "#8Z short": [6.83, 7.62],
        "#10": [15.79, 17.78],
        "#211": [6.83, 12.38],
        "#300": [7.62, 11.27],
        "#303": [8.10, 11.11]
    }

    for can in DATA:
        valuesList = DATA[can]
        radius = valuesList[0]
        height = valuesList[1]
        # print(f"{compute_volume(radius, height)}  {compute_surface_area(radius, height)}")
        

        print(f"{can} {compute_storage_efficiency(radius, height):.2f}")


def compute_volume(radius, height):
    return math.pi * pow(radius, 2) * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height) 

def compute_storage_efficiency(radius, height):
    return compute_volume(radius, height) / compute_surface_area(radius, height)

main()
