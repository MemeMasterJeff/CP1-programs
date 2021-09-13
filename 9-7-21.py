#William Wang
#9-7-21
#This program computes the final value of an invested amount using the compound interest formula:
#amount = principle * (1 + percentageRate / num) ** (num * term)

#Variables:
#  amount ........... Final value of investment
#  principle ........ Amount invested
#  rate ............. Rate of interest as a decimal
#  num .............. Number of times per year compounded
#  term ............. Investment term in years
#  percentageRate ... Rate of interest as a percentage

print("Welcome to the Investing Program \n")

#   Assign values of input data

principle = 4500
percentageRate = .096
term = 2
num = 12

#   Compute final value of investment
amount = principle * (1 + percentageRate / num) ** (num * term)
rate = percentageRate * 100

#   Display results

print("Amount of money invested ....", principle, "dollars")
print("Rate of interest ............", rate, "percent")
print("Frequency of compounding ....", num, "times per year")
print("Period of investment ........", term, "years")
print()
print("Final value of investment ...", amount, "dollars")

input("\nPress enter to exit")
