"""
def main():
    windowWidth = 2
    windowHeight = 3
    wallWidth = float(input("Wall width: "))
    wallHeight = float(input("Wall height: "))
    numberOfWindows = int(input("Number of windows: "))
    area = (wallWidth * wallHeight) - (numberOfWindows * (windowWidth * windowHeight))
    print("Area: ", area)
main()
"""
"""
def main():
    price = float(input("Unit price: "))

    print("Quantity     Price")
    quantity = 1
    print("%8d, %10.2f" % (quantity, quantity * price))
    quantity = 12
    print("%8d, %10.2f" % (quantity, quantity * price))
    quantity = 100
    print("%8d, %10.2f" % (quantity, quantity * price))
main()
"""

from ezgraphics import GraphicsWindow
