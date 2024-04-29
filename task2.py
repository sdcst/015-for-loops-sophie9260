#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  
Find the total value of all items and 
then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""
total = 0
for i in range(5):
    n = i + 1
    p  = input(f"Enter the price of the #{n} item => ")
    p = float(p)
    np = float(p)
    total = total + np

total  = round(total, 2)
print(f"The subtotal is {total}$.")

gst = 0.05*total
gst = round(gst, 2)
print(f"The GST is {gst}$.")

pst = 0.07*total
pst = round(pst, 2)
print(f"The PST is {pst}$.")

tt = total+pst+gst
tt = round(tt, 2)
print(f"The total is {tt}$.")
