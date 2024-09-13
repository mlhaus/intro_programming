def calculateFutureValue(monthlyInvestment, monthlyRate, months):
    futureValue = 0
    for i in range(months):
        futureValue = (futureValue + monthlyInvestment) * (1 + monthlyRate)
    return futureValue

print(calculateFutureValue(100, 0.06/12, 12))