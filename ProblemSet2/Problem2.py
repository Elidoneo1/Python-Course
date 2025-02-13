# Problem Set 2

#1
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def RemainingBalance(balance,annualInterestRate,monthlyPaymentRate,i=1):
    MonthlyInterestRate = annualInterestRate / 12
    MinimumMonthlyPayment = monthlyPaymentRate * balance
    MonthlyUnpaidBalance = balance - MinimumMonthlyPayment
    NewBalance = round(MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance,2)
    #print("Month ",i," Remaining balance: ",NewBalance)
    i += 1
    if i == 13:
        print("Remaining balance: ",NewBalance)
        return
    else:
        return RemainingBalance(NewBalance, annualInterestRate, monthlyPaymentRate,i)


RemainingBalance(balance, annualInterestRate, monthlyPaymentRate)

print(" ")


#2
balance = 320000
annualInterestRate = 0.2

def FixMonthlyPayment(balance,annualInterestRate,epsilon = 0.01):
    MonthlyInterestRate = annualInterestRate / 12
    low = balance / 12 #When annualInterestRate == 0, the balance is the fixed monthly payment
    high = (balance * (1 + annualInterestRate) ** 2)/ 12 #Maximum value without lowering the balance
    
    while high - low >= epsilon:
        monthlyPayment = (high + low) / 2
        TempBalance = balance
        #print("low: ",low,"high: ",high)
        #print("Calculating with monthlypayment of: ",monthlyPayment)
        for i in range(12):
            TempBalance = (TempBalance - monthlyPayment) * (1 + MonthlyInterestRate)
        
        if TempBalance > 0:
            low = monthlyPayment
        else:
            high = monthlyPayment
        #print("Balance: ",TempBalance)
    monthlyPayment = (monthlyPayment + 10) // 10 * 10
    print("Lowest Payment: ",monthlyPayment)


FixMonthlyPayment(balance, annualInterestRate)
print(" ")


#3
balance = 999999
annualInterestRate = 0.18

def FixMonthlyPayment(balance,annualInterestRate,epsilon = 0.01):
    MonthlyInterestRate = annualInterestRate / 12
    low = balance / 12 #When annualInterestRate == 0, the balance is the fixed monthly payment
    high = (balance * (1 + annualInterestRate) ** 2)/ 12 #Maximum value without lowering the balance
    
    while high - low >= epsilon:
        monthlyPayment = (high + low) / 2
        TempBalance = balance
        #print("low: ",low,"high: ",high)
        #print("Calculating with monthlypayment of: ",monthlyPayment)
        for i in range(12):
            TempBalance = (TempBalance - monthlyPayment) * (1 + MonthlyInterestRate)
        
        if TempBalance > 0:
            low = monthlyPayment
        else:
            high = monthlyPayment
        #print("Balance: ",TempBalance)
        monthlyPayment= round(monthlyPayment,2)
    print("Lowest Payment: ",monthlyPayment)


FixMonthlyPayment(balance, annualInterestRate)


