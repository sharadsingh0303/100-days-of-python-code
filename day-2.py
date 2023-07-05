# understanding data types and how to manipulate strings

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill amount?\n"))
tip = float(input("How much tip would you like to give?\n"))
split = float(input("How many people to split the bill?\n"))

total = ("{:.2f}".format(((bill * (tip/100) + bill) / split)))
print("Each person should pay : ", total)
