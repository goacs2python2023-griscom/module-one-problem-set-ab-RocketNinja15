import math
def calc():
    people = int(input("Amount of People:"))
    busses = people/52

    print("School Busses Needed:" + str(math.ceil(busses)))

calc()