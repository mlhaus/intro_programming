investment = 1000
number_of_years = 3
annual_interest_rate = 0.05
for i in range(number_of_years):
    yearly_interest = investment * annual_interest_rate
    investment += yearly_interest
print(round(investment, 2)) # print the investment with 20 years of interest added