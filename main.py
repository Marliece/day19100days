print("Loan Calculator")
print()

loan = 1000
apr = 0.05
t = 10

print("$",loan," over",t, "years at", apr,"% APR")
print()

loan_amount = loan*apr

for year in range(10):
  year += 1
  loan += (loan*apr)
  print("Year", year, "is", round(loan, 2))
  