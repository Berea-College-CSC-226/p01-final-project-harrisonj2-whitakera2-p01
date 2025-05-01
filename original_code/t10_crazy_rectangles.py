######################################################################
# Author: Dr. Scott Heggen         TODO: Change this to your names
# Username: heggens                TODO: Change this to your usernames
#
# Assignment: T10: Intro to Classes
#
# Purpose:  Demonstrate the collaboration between classes,
#           such as using a point to create a rectangle
######################################################################
# Acknowledgements:
#
# Original code created by Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import t10_rectangle as rectangle  # notice the different ways we can import, and how that changes how we use it below
from t10_point import Point        # and again...
import random
import turtle


def main():
    """
    Draws 25 randomly placed, randomly sized, randomly colored rectangles using the turtle library.
    The code demonstrates interactions between classes, such as the use of a Point
    object to create a Rectangle object.

    :return: None
    """
    wn = turtle.Screen()
    wn.colormode(255)

    for i in range(25):
        # each loop iteration, a new point object at a random (x, y) coordinate
        randx = random.randrange(500)-250
        randy = random.randrange(500)-250
        pt = Point(randx, randy)

        # a rectangle object which starts at the point defined above
        randw = random.randrange(i+100)
        randh =  random.randrange(i+100)
        rect = rectangle.Rectangle(pt, randw, randh)

        # calls the draw_rectangle method of the Rectangle object
        randr = random.randrange(255)
        randg = random.randrange(255)
        randb = random.randrange(255)
        randa = random.randrange(360)
        rect.draw_rectangle(randr, randg, randb, randa)

    wn.exitonclick()


if __name__ == "__main__":
    main()
