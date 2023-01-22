def tipcalculator():
    bill = int(input("Subtotal:"))
    tip = int(input("Tip %:"))
    bill = (tip/100)*bill + bill
    print(bill)
tipcalculator()