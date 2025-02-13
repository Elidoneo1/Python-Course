#1
balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def RemainingBalance(balance,annualInterestRate,monthlyPaymentRate,i=1):
    MonthlyInterestRate = annualInterestRate / 12
    MinimumMonthlyPayment = monthlyPaymentRate * balance
    MonthlyUnpaidBalance = balance - MinimumMonthlyPayment
    NewBalance = round(MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance,2)
    i += 1
    if i == 13:
        print("Remaining balance: ",NewBalance)
        return
    else:
        return RemainingBalance(NewBalance, annualInterestRate, monthlyPaymentRate,i)


RemainingBalance(balance, annualInterestRate, monthlyPaymentRate)

print(" ")


#2
balance = 4773
annualInterestRate = 0.2

def FixMonthlyPayment(balance,annualInterestRate,epsilon = 0.01):
    MonthlyInterestRate = annualInterestRate / 12
    low = balance / 12 
    high = (balance * (1 + annualInterestRate) ** 2)/ 12
    
    while high - low >= epsilon:
        monthlyPayment = (high + low) / 2
        TempBalance = balance
        for i in range(12):
            TempBalance = (TempBalance - monthlyPayment) * (1 + MonthlyInterestRate)
        
        if TempBalance > 0:
            low = monthlyPayment
        else:
            high = monthlyPayment
    monthlyPayment = (monthlyPayment + 10) // 10 * 10
    print("Lowest Payment: ",monthlyPayment)


FixMonthlyPayment(balance, annualInterestRate)
print(" ")


#3
balance = 3926
annualInterestRate = 0.2

def FixMonthlyPayment(balance,annualInterestRate,epsilon = 0.01):
    MonthlyInterestRate = annualInterestRate / 12
    low = balance / 12
    high = (balance * (1 + annualInterestRate) ** 2)/ 12 
    
    while high - low >= epsilon:
        monthlyPayment = (high + low) / 2
        TempBalance = balance
        for i in range(12):
            TempBalance = (TempBalance - monthlyPayment) * (1 + MonthlyInterestRate)
        
        if TempBalance > 0:
            low = monthlyPayment
        else:
            high = monthlyPayment
        monthlyPayment= round(monthlyPayment,2)
    print("Lowest Payment: ",monthlyPayment)


FixMonthlyPayment(balance, annualInterestRate)


