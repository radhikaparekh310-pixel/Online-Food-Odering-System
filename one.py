# Project: Online Food Ordering System
# PS No. 44
# Language: Python 3

# Food Menu
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

# Shopping Cart
cart = []


# Display Food Menu
def show_menu():
    print("\n========== FOOD MENU ==========")
    for item, price in menu.items():
        print(f"{item}: Rs. {price}")
    print("===============================")


# Calculate Cart Subtotal
def calculate_subtotal():
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]
    return subtotal


# Add Item to Cart
def add_item():
    show_menu()

    item_name = input("Enter item name: ").strip().title()

    if item_name not in menu:
        print("Item not available. Please choose from Burger, Pizza, Fries, Coke.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Invalid quantity. Enter a positive number.")
            return

    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    for item in cart:
        if item["name"] == item_name:
            item["quantity"] += quantity
            break
    else:
        cart.append({
            "name": item_name,
            "price": menu[item_name],
            "quantity": quantity
        })

    print(f"{item_name} x{quantity} added to cart.")
    print("Cart subtotal:", calculate_subtotal())


# Remove Item from Cart
def remove_item():
    if not cart:
        print("Your cart is empty.")
        return

    item_name = input("Enter item name to remove: ").strip().title()

    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            print(item_name, "removed from cart.")
            return

    print("Item not found in cart.")


# Display Cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    for item in cart:
        amount = item["price"] * item["quantity"]
        print(f"{item['name']} x{item['quantity']} = Rs. {amount}")

    print("-------------------------------")
    print("Cart Subtotal: Rs.", calculate_subtotal())


# Apply Coupon
def apply_coupon(subtotal, coupon):
    if coupon == "":
        return 0

    if coupon == "SAVE10":
        discount = subtotal * 0.10
        print("Coupon SAVE10 applied successfully!")
        return discount

    print("Invalid coupon code. Only SAVE10 is accepted.")
    return 0


# Checkout and Generate Bill
def checkout():
    if not cart:
        print("Your cart is empty. Add items first.")
        return

    subtotal = calculate_subtotal()

    coupon = input("Enter coupon code (Press Enter to skip): ")
    coupon = coupon.strip().upper()

    discount = apply_coupon(subtotal, coupon)

    amount_after_discount = subtotal - discount
    gst = amount_after_discount * 0.05

    if subtotal >= 300:
        delivery = 0
    else:
        delivery = 40

    total = amount_after_discount + gst + delivery

    print("\n========== FINAL BILL ==========")

    for item in cart:
        amount = item["price"] * item["quantity"]
        print(f"{item['name']} x{item['quantity']} = Rs. {amount}")

    print("--------------------------------")
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"GST (5%): Rs. {gst:.2f}")
    print(f"Delivery: Rs. {delivery:.2f}")
    print("--------------------------------")
    print(f"Total Amount: Rs. {total:.2f}")
    print("Thank you for ordering!")
    print("================================")


# Main Program
def main():
    while True:
        print("\n===== ONLINE FOOD ORDERING SYSTEM =====")
        print("1. Show Food Menu")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_item()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("Thank you! Visit again.")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")


# Run the Program
if __name__ == "__main__":
    main()