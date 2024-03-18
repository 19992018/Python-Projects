# create a dictionary whose key is branch and value is an empty array
# the empty array will store all the item totals
kori_supermarket = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
# make a list out of the keys in kori supermarket
expected_inputs = kori_supermarket.keys()  # = ['A', 'B', 'C', 'D', 'E']

# create an endless loop to take in all supermarkets' data endlessly
while True:
    branch = input("Branch: ").upper()
    # condition to terminate loop
    if branch == "END":
        # terminate loop only if we have more than 6 items
        if len(kori_supermarket['A']) < 2 or len(kori_supermarket['B']) < 2 or len(kori_supermarket['C']) < 2 or len(kori_supermarket['D']) < 2 or len(kori_supermarket['E']) < 2:
            print("Error: Please enter at least six items for all the branches ")
            continue
        else:
            break
    # checking if input (branch name) makes sense
    if expected_inputs.__contains__(branch):
        print("Key in the following data for branch " + branch)
    else:
        print("Key in the correct branch name")
        continue

    print(kori_supermarket)

    code = input("enter code: ")
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))
    item_price = unit_price * quantity

    # update dictionary only if the branch is A/B/C...
    if branch != 'END':
        kori_supermarket[branch].append(item_price)
    print("DATA: " + str(kori_supermarket))
    print("Total so far for kori " + branch + " is " + str(sum(kori_supermarket[branch])))
    print(" ")

# calculate grand total
grand_total = 0
for branch in kori_supermarket:
    branch_total = sum(kori_supermarket[branch])
    kori_supermarket[branch] = branch_total
    grand_total = grand_total + branch_total
print("Below is each Kori Branch with its subtotal: ")
print(kori_supermarket)
print("The grand total sale for all kori supermarkets is " + str(grand_total))




