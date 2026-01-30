import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def display_menu():
    print("\nStore Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def process_order(store_obj):
    available_products = store_obj.get_all_products()
    if not available_products:
        print("Store is currently empty.")
        return

    print("\nAvailable products:")
    for i, p in enumerate(available_products, start=1):
        print(f"{i}. ", end="")
        p.show()

    shopping_list = []
    print("\nEnter product number and quantity. Type 'done' to finish.")

    while True:
        user_input = input("Product number (or 'done'): ").lower()
        if user_input == 'done':
            break

        try:
            prod_idx = int(user_input) - 1
            if prod_idx < 0 or prod_idx >= len(available_products):
                print("Invalid product number.")
                continue

            qty_input = input("Quantity: ")
            qty = int(qty_input)

            product = available_products[prod_idx]
            shopping_list.append((product, qty))
            print("Added to cart.")

        except ValueError:
            print("Invalid input. Please enter numbers or 'done'.")

    if shopping_list:
        try:
            total_price = store_obj.order(shopping_list)
            print(f"**********\nOrder done! Total price: {total_price:,.2f}\n**********")
        except Exception as e:
            print(f"Order failed: {e}")


def start(store_obj):
    while True:
        display_menu()
        choice = input("Choose a number: ")

        if choice == "1":
            for i, p in enumerate(store_obj.get_all_products(), start=1):
                print(f"{i}. ", end="")
                p.show()
        elif choice == "2":
            print(f"Total amount in store: {store_obj.get_total_quantity()}")
        elif choice == "3":
            process_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)
