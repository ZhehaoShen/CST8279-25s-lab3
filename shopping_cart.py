# Author: Zhehao Shen
# Date: 2025-05-25
# This program simulates a simple shopping cart.
# Users can add items, specify quantities, and see the total cost.
# The program uses exception handling to manage invalid inputs.

print("Welcome to the Shopping Cart Program!")

def shopping_cart():
    while True:
        cart = []

        # Step 1: Ask the user for the number of items
        try:
            num_items = int(input("How many items would you like to add to your cart? (Max 3): "))
            if num_items > 3 or num_items < 1:
                print("Invalid input. You can add up to 3 items.")
                num_items = 3
        except ValueError:
            print("Invalid input. Defaulting to 3 items.")
            num_items = 3

        # Step 2: Ask for item name, price, and quantity
        for i in range(num_items):
            print(f"\nItem {i + 1}:")

            name = input("Enter the item name: ")

            while True:
                try:
                    price = float(input("Enter the item price: $"))
                    if price < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid, non-negative number for price.")

            while True:
                try:
                    quantity = int(input("Enter the quantity: "))
                    if quantity < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid, non-negative integer for quantity.")

            # Store item in a dictionary and append to the cart
            item = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            cart.append(item)

        # Step 3: Calculate total cost
        total = 0
        print("\n--- Shopping Cart Summary ---")
        for item in cart:
            item_total = item["price"] * item["quantity"]
            total += item_total
            print(f"{item['quantity']} x {item['name']} @ ${item['price']:.2f} each = ${item_total:.2f}")

        # Apply discount if applicable
        if total > 100:
            discount = total * 0.1
            total -= discount
            print(f"\nYou saved ${discount:.2f} with a 10% discount!")
            print(f"Discounted Total: ${total:.2f}")
        else:
            print(f"\nTotal cost: ${total:.2f}")

        # Ask if user wants to restart
        restart = input("\nWould you like to shop again? (yes/no): ").lower()
        if restart == "yes":
            continue
        else:
            print("Thank you for shopping with us!")
            break

if __name__ == "__main__":
    shopping_cart()