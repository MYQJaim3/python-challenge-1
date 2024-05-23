# Initialize an empty list to store the customer's order
order = []

# Define the menu items
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49}
}

# Start the ordering process
place_order = True
while place_order:
    # Print the menu
    for key, value in menu_items.items():
        print(f"{key}: {value['Item name']} - ${value['Price']:.2f}")

    # Prompt the customer to enter their selection
    menu_selection = input("Please enter the number of the item you would like to order: ")

    # Check if the input is a number
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    # Convert the input to an integer
    menu_selection = int(menu_selection)

    # Check if the input is in the keys of menu_items
    if menu_selection not in menu_items.keys():
        print("Invalid selection. Please choose a number from the menu.")
        continue

    # Get the item name and price
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]

    # Ask the customer for the quantity
    quantity = input(f"How many {item_name}s would you like to order? (Quantity will default to 1 if input is invalid): ")

    # Check if the input is a number
    if not quantity.isdigit():
        quantity = 1
    else:
        # Convert the input to an integer
        quantity = int(quantity)

    # Append the order to the list
    order.append({"Item name": item_name, "Price": price, "Quantity": quantity})

    # Ask the customer if they would like to keep ordering
    while True:
        continue_ordering = input("Would you like to order another item? (y/n): ").lower()
        if continue_ordering == 'y':
            break
        elif continue_ordering == 'n':
            place_order = False
            print("Thank you for your order.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Print the receipt
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # Calculate the number of empty spaces
    item_name_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (8 - len(str(price)))

    # Print the line for the receipt
    print(f"{item_name}{item_name_spaces}| ${price:.2f}{price_spaces}| {quantity}")

# Calculate the total price of the order
total_price = sum([item["Price"] * item["Quantity"] for item in order])
print(f"\nTotal: ${total_price:.2f}")
