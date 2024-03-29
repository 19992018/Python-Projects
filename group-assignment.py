import random
# dictionary contains supermarket name as key and supermarket total as value
kori_supermarket = {
    "kori_A": 0,
    "kori_B": 0,
    "kori_C": 0,
    "kori_D": 0,
    "kori_E": 0,
}
# We make a list out of the keys of our supermarket dictionary
branch = list(kori_supermarket.keys())

# We loop through the list we created
for key in branch:
    price = []
    print(f"branch of {key}")
    print('enter "end" when you finish')

    # We endlessly process the items per supermarket
    while True:
        code = input("enter code: ").lower()
        # We key in end to end the processing of items
        if code == "end":
            # processing of items ends only ends if we have more than 6 items
            if len(price) < 6:
                print("Error: Please enter at least six items.")
                continue
            else:
                break
        unit_price = float(input("enter unit price: "))
        quantity = int(input("enter quantity: "))
        item_total = quantity * unit_price
        # We append total per item to empty price list
        price.append(item_total)
        print(f"item total is {item_total}")
        print(" ")

    # Get the sum of the price array
    total_price = sum(price)
    kori_supermarket[key] = total_price
    print("Total amount for " + key + " is " + str(total_price))
    print(" ")

print("Here is each branch with its total : ")
print(kori_supermarket)
# Get the sum of the values of the kori supermarket dictionary (grand total)
grand_total = sum(kori_supermarket.values())
print(f"The grand total is {grand_total}")
