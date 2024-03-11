#A customer has bought two different items from a shop. Item A costs Kshs 500 a piece while item B costs Kshs 200 a piece.
# He has bought 5 units of item A and 10 units of item B.
# Write the following functions:
#1.	A function to calculate the total amount spent on the items
#2.	A  function to apply a discount of 15% on the total price.
#3.	A function to calculate and display the NET amount to be paid after the application of the discount.

def calculate_total():
    total= 500*5+200*10
    return total

def calculate_discount():
    discount = 0.15*calculate_total()
    return discount

def net_total():
    to_pay= calculate_total()-calculate_discount()
    return to_pay

print(net_total())

