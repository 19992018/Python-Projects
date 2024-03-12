# create a supermarkets dictionary
# the keys are the supermarket names the values are the subtotals per supermarket
supermarkets = {"KORI A": 0, "KORI B": 0, "KORI C": 0, "KORI D": 0, "KORI E": 0, }

# we loop through the supermarkets dictionary keys
for supermarket in supermarkets:
    print("Taking in data for " + supermarket)

    # create empty list that will store item totals
    # we will use this later to calculate subtotal
    store_subtotal = []
    # Take in code, price and quantity for 6 items
    for i in range(6):
        # Take the inputs
        code = input("item code: ")
        unit_price = int(input("unit price: "))
        quantity = int(input("quantity: "))

        # calculate the item total...
        item_total = unit_price * quantity

        # keep track of item totals by storing in store subtotal
        store_subtotal.append(item_total)

        # print item total
        print("item total is: " + str(item_total))

        # use method sum(list) to calculate subtotal
        print("subtotal is: " + str(sum(store_subtotal)))
        print(" ")

    # The final subtotal for each supermarket is its eventual supermarket total
    print("Total for supermarket " + supermarket + " is " + str(sum(store_subtotal)))
    print(" ")

    # We update the value of each key in supermarkets dictionary after every iteration
    supermarkets[supermarket] = sum(store_subtotal)

print("Below is each supermarket with its total: ")
print(supermarkets)
# We calculate the grand total by getting the sum of the values in supermarkets dictionary
print("The grand total is " + str(sum(supermarkets.values())))

