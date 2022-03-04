#!/usr/bin/env python3
# Created by: Sarah
# Created on: Mar. 4, 2022
# This program asks the user for the length and
# width of the rectangle in cm. It then
# calculates and displays the area and
# perimeter.
import math


def main():
    # Input of the user
    print("Today, we will be calculating the area and")
    print("perimeter of a rectangle")
    length = int(input("Enter the length of the rectangle (cm): "))
    width = int(input("Enter the width of the rectangle (cm): "))

    # Calculate area & perimeter
    area = length * width
    perimeter = 2*(length + width)

    # Display results
    print("")
    print("Area = {} cm^2". format(area))
    print("Perimeter = {} cm". format(perimeter))


if __name__ == "__main__":
    main()
