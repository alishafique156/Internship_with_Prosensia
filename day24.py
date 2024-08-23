def add_product(inventory):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    for product in inventory:
        if product['name'] == name:
            print(f"Product '{name}' already exists in the inventory.")
            return

    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print(f"Product '{name}' added successfully.")

def update_product_quantity(inventory):
    name = input("Enter product name to update quantity: ")
    for product in inventory:
        if product['name'] == name:
            quantity = int(input("Enter new quantity: "))
            product['quantity'] = quantity
            print(f"Quantity for '{name}' updated successfully.")
            return
    print(f"Product '{name}' not found in the inventory.")

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("Current Inventory:")
    for product in inventory:
        print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def main():
    inventory = []
    
    while True:
        print("\n1. Add Product")
        print("2. Update Product Quantity")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_product_quantity(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
