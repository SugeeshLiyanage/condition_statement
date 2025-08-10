actual_amount = float(input("enter actual price"))
selling_amount = float(input("enter the selling price"))
if actual_amount < selling_amount:
 profit = selling_amount - actual_amount
 print(profit)
else:
 print("no money made!!!")