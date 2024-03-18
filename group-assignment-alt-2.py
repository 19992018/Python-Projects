import random
kori_supermarket = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
expected_inputs = ['A', 'B', 'C', 'D', 'E']
item_price = 0
while True:
    branch = input("Branch: ").upper()
    if branch == "END":
        # processing of items ends only ends if we have more than 6 items
        # for letter in expected_inputs:
        if len(kori_supermarket['A']) < 2 or len(kori_supermarket['B']) < 2 or len(kori_supermarket['C']) < 2 or len(kori_supermarket['D']) < 2 or len(kori_supermarket['E']) < 2:
            print("Error: Please enter at least six items for all the branches ")
            continue
        else:
            break
    if expected_inputs.__contains__(branch):
        # kori_supermarket[branch] = [item_price]
        print("Key in the following data for branch " + branch)
    else:  # branch == "A" or "B" or "C" or "D" or "E"
        print("Key in the correct branch name")
        continue
    print(kori_supermarket)

    code = input("enter code: ")
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))
    item_price = unit_price * quantity

    if branch != 'END':
        kori_supermarket[branch].append(item_price)
    print("DATA: " + str(kori_supermarket))
    print("Total so far for kori " + branch + " is " + str(sum(kori_supermarket[branch])))
    print(" ")

display_totals = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
grand_total = 0
for branch in display_totals:
    branch_total = sum(kori_supermarket[branch])
    display_totals[branch] = branch_total
    grand_total = grand_total + branch_total
print("Below is each Kori Branch with its subtotal: ")
print(display_totals)
print("The grand total sale for all kori supermarkets is " + str(grand_total))




