def payingMinimum():
    count = 0
    monthlyRate = 0.02
    balance = float(input("Balance: "))
    while True:
        balance = 1.015 * (balance - (balance * monthlyRate))
        count += 1
        if count == 12:
            print(balance)
            break
    # monthlyRate = 1 - (newBalance / (1.015 * balance))
    
def payingDebtInYear():
    # OBJECTIVE: find monthlyRate
    count = 0
    balance = float(input("Balance: "))
    payment = balance / 12
    payment = payment * 1.1006
    fixedPayment = payment
    while True:
        unpaid = balance - fixedPayment
        interest = 0.015 * unpaid
        balance = interest + unpaid
        if count == 12:
            print(balance)
            break
        
# payingMinimum()
payingDebtInYear()
     