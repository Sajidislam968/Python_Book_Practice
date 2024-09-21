investmentAmount = int(input("Enter Investment Amount: "))
monthlyInterestRate = float(input("Enter Monthly Interest Rate: "))*(1/100)
numberOfMonths = int(input("Enter Number of Months: "))
futureInvestment = investmentAmount*(1+monthlyInterestRate)**numberOfMonths
print("Accumulated value is ", futureInvestment)