def calcuation():
    distance = int(input("Total Distance Traveled: "))
    mpg = int(input("Car MPG: "))
    gasprice = int(input("Cost Of Gas: "))
    return (distance/mpg)*gasprice

print(calcuation())