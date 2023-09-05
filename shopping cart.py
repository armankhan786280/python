class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product_name):
        for item in self.items:
            if item['product'].name == product_name:
                self.items.remove(item)
                return

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your shopping cart:")
            for item in self.items:
                print(f"{item['product'].name} - Price: ${item['product'].price} - Quantity: {item['quantity']}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

def main():
    cart = ShoppingCart()

    while True:
        print("\nMenu:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_name = input("Enter the product name: ")
            product_price = float(input("Enter the product price: "))
            product_quantity = int(input("Enter the quantity: "))
            product = Product(product_name, product_price)
            cart.add_item(product, product_quantity)
            print(f"{product_name} has been added to your cart.")

        elif choice == '2':
            product_name = input("Enter the product name to remove: ")
            cart.remove_item(product_name)
            print(f"{product_name} has been removed from your cart.")

        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            total = cart.calculate_total()
            print(f"Total cost of items in your cart: ${total}")

        elif choice == '5':
            print("Thank you for shopping with us! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()