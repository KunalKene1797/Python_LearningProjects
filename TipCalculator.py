print("How much did the meal cost?")
meal = float(input())
print("Welcome, How Much is the Tax Percentage?")
taxno = float(input())
tax = taxno / 100
print("How much is the tip percentage?")
tipno = float(input())
tip = tipno / 100
total = meal + meal*tax + meal*tip
print("The Total Bill Will Be =>", total)
print("The Tax Will Be =>", meal*tax)
print("The Tip Will Be =>", meal*tip)
print("Press Any Key To Exit")
input()
exit()
