def add_product(inventory):
    name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory.append({"name": name, "id": product_id, "quantity": quantity, "price": price})

def view_inventory(inventory):
    if not inventory:
        print("No products available in inventory.")
    else:
        for product in inventory:
            print(f"Name: {product['name']}, ID: {product['id']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")

def update_product_quantity(inventory):
    product_id = input("Enter product ID to update: ")
    for product in inventory:
        if product['id'] == product_id:
            new_quantity = int(input(f"Enter new quantity for {product['name']}: "))
            product['quantity'] = new_quantity
            print(f"Quantity updated for {product['name']}.")
            return
    print("Product ID not found.")

def remove_product(inventory):
    product_id = input("Enter product ID to remove: ")
    for product in inventory:
        if product['id'] == product_id:
            inventory.remove(product)
            print(f"Product {product['name']} removed from inventory.")
            return
    print("Product ID not found.")

def main():
    inventory = []
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_product_quantity(inventory)
        elif choice == "4":
            remove_product(inventory)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

main()
