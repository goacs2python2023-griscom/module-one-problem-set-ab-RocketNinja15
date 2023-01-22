import random
def dicetwo():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    totaldice = d1+d2
    if(totaldice == 6 or totaldice == 7 or totaldice == 8):
        print("Win!")
    else:
        print("Lose")

    print(totaldice)

dicetwo()