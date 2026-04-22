# ===================== PRODUCT =====================
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


# ===================== STORE =====================
class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.pid] = product
        print("✅ Product added successfully")

    def view_products(self):
        if not self.products:
            print("❌ No products available")
            return

        print("\n--- Available Products ---")
        for p in self.products.values():
            print(f"{p.pid} | {p.name} | ₹{p.price}")


# ===================== SHOPPING CART =====================
class ShoppingCart:
    def __init__(self):
        self.items = {}  # pid : quantity

    def add_to_cart(self, pid, qty):
        self.items[pid] = self.items.get(pid, 0) + qty
        print("🛒 Item added to cart")

    def remove_from_cart(self, pid):
        if pid in self.items:
            del self.items[pid]
            print("🗑️ Item removed from cart")
        else:
            print("❌ Item not in cart")

    def view_cart(self, store):
        if not self.items:
            print("🛒 Cart is empty")
            return

        print("\n--- Your Cart ---")
        for pid, qty in self.items.items():
            p = store.products[pid]
            print(f"{p.name} | ₹{p.price} | Qty: {qty}")

    def total_amount(self, store):
        return sum(store.products[pid].price * qty for pid, qty in self.items.items())


# ===================== USER =====================
class User:
    def __init__(self, username):
        self.username = username


# ===================== ADMIN =====================
class Admin(User):
    def admin_menu(self, store):
        while True:
            print("\n--- ADMIN MENU ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                pid = int(input("Product ID: "))
                name = input("Product Name: ")
                price = int(input("Price: "))
                store.add_product(Product(pid, name, price))

            elif choice == "2":
                store.view_products()

            elif choice == "3":
                break

            else:
                print("❌ Invalid choice")


# ===================== CUSTOMER =====================
class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.cart = ShoppingCart()

    def customer_menu(self, store):
        while True:
            print(f"\n--- CUSTOMER MENU ({self.username}) ---")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                store.view_products()

            elif choice == "2":
                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter Quantity: "))
                if pid in store.products:
                    self.cart.add_to_cart(pid, qty)
                else:
                    print("❌ Invalid Product ID")

            elif choice == "3":
                pid = int(input("Enter Product ID: "))
                self.cart.remove_from_cart(pid)

            elif choice == "4":
                self.cart.view_cart(store)

            elif choice == "5":
                total = self.cart.total_amount(store)
                print(f"\n💰 Total Bill: ₹{total}")
                print("✅ Order placed successfully 🎉")
                break

            elif choice == "6":
                break

            else:
                print("❌ Invalid choice")


# ===================== MAIN =====================
def main():
    store = Store()

    while True:
        print("\n=== ONLINE SHOPPING SYSTEM ===")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        role = input("Select role: ")

        if role == "1":
            admin = Admin("Admin")
            admin.admin_menu(store)

        elif role == "2":
            name = input("Enter your name: ")
            customer = Customer(name)
            customer.customer_menu(store)

        elif role == "3":
            print("🙏 Thank you for using the system")
            break

        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()