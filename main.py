import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def start(store_obj):
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Choose a number: ")

        if choice == "1":
            products_list = store_obj.get_all_products()
            for i, p in enumerate(products_list, start=1):
                print(str(i) + ".", end=" ")
                p.show()

        elif choice == "2":
            total = store_obj.get_total_quantity()
            print("Total amount in store:", total)

        elif choice == "3":
            products_list = store_obj.get_all_products()
            print("What do you want to buy?")

            for i, p in enumerate(products_list, start=1):
                print(str(i) + ".", end=" ")
                p.show()

            product_number = int(input("Enter product number: "))
            quantity = int(input("Enter quantity: "))

            product = products_list[product_number - 1]
            total_price = store_obj.order([(product, quantity)])

            print("Order done! Total price:", total_price)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


def main():
    start(best_buy)


if __name__ == "__main__":
    main()
