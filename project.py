import os
import json
import bcrypt
from datetime import datetime


def save_credentials(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    credentials = {
        'username': username,
        'password': hashed_password.decode('utf-8')
    }
    with open('credentials.json', 'w') as file:
        json.dump(credentials, file)


def authenticate(username, password):
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)
        saved_username = credentials['username']
        saved_password = credentials['password']

        if username == saved_username and bcrypt.checkpw(password.encode('utf-8'), saved_password.encode('utf-8')):
            print("Authentication successful!")
        else:
            print("Authentication failed!")
            run_program()


def run_program():
    try:
        with open('credentials.json', 'r') as file:
            credentials = json.load(file)
            saved_username = credentials['username']
            saved_password = credentials['password']

        username = input("Enter username: ")
        password = input("Enter password: ")

        authenticate(username, password)

    except FileNotFoundError:
        username = input("Enter username: ")
        password = input("Enter password: ")

        save_credentials(username, password)
        print("Credentials saved!")


# Function to load products from a file
def load_products():
    if os.path.exists("products.json"):
        with open("products.json", "r") as file:
            return json.load(file)
    else:
        return []


# Function to load balance from a file
def load_balance():
    if os.path.exists("balance.txt"):
        with open("balance.txt", "r") as file:
            return float(file.read())
    else:
        return 0.0


# Function to save products to a file
def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file)


# Function to save balance to a file
def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))


# Function to add a new product
def add_product(products):
    print("Add a New Product:")

    # Collect product information from the user
    product_name = input("Enter product name: ")
    category = input("Enter product category: ")
    dose = input("Enter product dose: ")
    price = float(input("Enter product price: "))
    description = input("Enter product description: ")
    stock_quantity = int(input("Enter stock quantity: "))
    expiry_date_str = input("Enter expiry date (DD-MM-YYYY): ")

    # Create a new product dictionary
    new_product = {
        "name": product_name,
        "category": category,
        "dose": dose,
        "price": price,
        "description": description,
        "stock_quantity": stock_quantity,
        "expiry_date": expiry_date_str,
    }

    # Add the product to the list
    products.append(new_product)

    # Save the updated product list to the file
    save_products(products)

    print("Product added successfully!")

    # Function to delete a product


def delete_product(products):
    print("Delete a Product:")

    # Display available products
    display_products(products)

    # Ask the user to choose a product to delete
    product_name = input("Enter the name of the product to delete: ")

    # Check if the product exists
    found = False
    for product in products:
        if product["name"] == product_name:
            found = True
            break

    if found:
        # Remove the selected product in the original list
        products[:] = [product for product in products if product["name"] != product_name]

        # Save the updated product list to the file
        save_products(products)

        print(f"Product '{product_name}' deleted successfully!")
    else:
        print(f"Product '{product_name}' not found.")


# Function to display products
def display_products(products):
    if not products:
        print("No products available.")
        return

    print("\nProduct List:")
    print("{:<20} {:<15} {:<10} {:<10} {:<30} {:<15} {:<15}".format(
        "Product Name", "Category", "Dose", "Price", "Description", "Stock Quantity", "Expiry Date"
    ))
    print("-" * 130)

    for product in products:
        print("{:<20} {:<15} {:<10} ${:<10} {:<30} {:<15} {:<15}".format(
            product["name"],
            product["category"],
            product["dose"],
            product["price"],
            product["description"],
            product["stock_quantity"],
            product["expiry_date"],
        ))


# Function to sell a product
def sell_product(products, balance):
    print("Sell a Product:")

    # Display available products
    display_products(products)

    # Ask the user to choose a product to sell
    product_name = input("Enter the name of the product to sell: ")

    # Check if the product exists
    found = False
    for product in products:
        if product["name"] == product_name:
            found = True
            break

    if found:
        # Ask for the quantity to sell
        quantity = int(input(f"Enter the quantity of '{product_name}' to sell: "))

        # Check if there is enough stock
        if quantity <= product["stock_quantity"]:
            # Update product stock and balance
            product["stock_quantity"] -= quantity
            balance += quantity * product["price"]

            # Save the updated product list to the file
            save_products(products)

            # Save the updated balance to a file
            save_balance(balance)

            print(f"Sold {quantity} units of '{product_name}' for ${quantity * product['price']}.")

            # Generate and print the bill
            generate_bill(products, {"name": product["name"], "quantity": quantity})
        else:
            print("Not enough stock available.")
    else:
        print(f"Product '{product_name}' not found.")


# Function to generate a bill for a sold product
def generate_bill(products, sold_product):
    print("Generating Bill:")

    # Find the sold product in the list
    for product in products:
        if product["name"] == sold_product["name"]:
            # Print the bill details
            print("\nReceipt:")
            print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Product Name: {product['name']}")
            print(f"Price per unit: ${product['price']}")
            print(f"Quantity Sold: {sold_product['quantity']}")
            print(f"Total Amount: ${sold_product['quantity'] * product['price']}")
            print("\nThank you for your purchase!")
            break


#Function to check the balance
def check_balance():
    if os.path.exists("balance.txt"):
        with open("balance.txt", "r") as file:
            print("Total sales :" + str(file.read()))


# Function to search for a product
def search_product(products):
    print("Search for a Product:")

    # Ask the user for the product name or other criteria
    search_query = input("Enter the product name or other criteria to search: ")

    # Create a list to store matching products
    matching_products = []

    # Search for products that match the criteria
    for product in products:
        if search_query.lower() in product["name"].lower() or search_query.lower() in product["category"].lower():
            matching_products.append(product)

    # Display the matching products
    if matching_products:
        print("\nMatching Products:")
        display_products(matching_products)
    else:
        print("No matching products found.")


# Main function
def main():
    run_program()
    # Load existing products and balance
    products = load_products()
    balance = load_balance()

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Display Products")
        print("4. Sell Product")
        print("5. Check Balance")
        print("6. Search Product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            delete_product(products)
        elif choice == "3":
            display_products(products)
        elif choice == "4":
            sell_product(products, balance)
        elif choice == "5":
            check_balance()
        elif choice == "6":
            search_product(products)
        elif choice == "7":
            # Save products and balance to files before exiting
            save_products(products)
            save_balance(balance)
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
