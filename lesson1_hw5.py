rev = float(input("Enter company's revenue: "))
exps = float(input("Enter company's expenses: "))

if rev > exps:
    print("Your performance: profit")
    profit = rev - exps
    margin = profit / rev * 100
    print(f"Profit margin = {margin:.2f}%")
    empl = int(input("Enter number of employees: "))
    n = profit / empl
    print(f"Profit per employee = {n:.2f}")
else:
    print("Your performance: loss")
