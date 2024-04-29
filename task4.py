"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""
balance = 0
total = 0

for i in range (2):
    n = 0
    n = i +1 
    tp = input(f"Enter the total of your purchases of the #{n} month => ")
    tp =  float(tp)
    po = input(f"Now enter how much you have paid off for the #{n} month => ")
    po = float(po)
    total  = tp - po
    total = total + balance
    interest = total*0.02
    interest = round(interest, 2)
    print(f"2% interest has been charged : {interest}$. ")
    balance = total + interest
    balance = round(balance, 2)
    print(f"The closing balance is {balance}$.")