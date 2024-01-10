# Pharmacy Management System Overview

terminal-based pharmacy management system program

This was a project done for programming for engineers course in university


## Features:

### 1. Authentication System:
- Secure login with a username and password.
- Passwords are hashed using the `bcrypt` library for enhanced security.
- Initial setup prompts users to set a username and password or reconfigure if the `credentials.json` file is missing.

### 2. Product Management:
- Maintain a comprehensive list of products stored in `products.json`.
- Add new products with detailed specifications: name, category, dose, price, description, stock quantity, and expiry date.
- Delete products based on their name.
- Display products in an organized tabular format, showcasing essential details.

### 3. Sales Management:
- Efficiently sell products with automatic stock quantity updates.
- Calculate total sales amounts for each transaction.
- Generate detailed bills for sales transactions, including product name, price per unit, sold quantity, and total amount.

### 4. Financial Management:
- Track total sales and revenue with a dedicated balance feature.
- Real-time balance updates stored in `balance.txt`.
- User-friendly balance checking mechanism to monitor sales performance.

### 5. Product Search:
- Robust product search functionality based on product names or categories.
- Display matching products in a structured manner for easy reference.

### 6. User Interface:
- Intuitive command-line interface offering streamlined functionalities.
- Main menu provides quick access to essential operations: add, delete, display, sell, check balance, search, and exit.

### 7. File Management:
- Efficient file handling for product data, balance records, and user credentials.
- Read and write operations to manage product details (`products.json`), financial records (`balance.txt`), and user authentication (`credentials.json`).

---

## Usage:

### - Setup:
- Upon initial use or if `credentials.json` is missing, the system guides users to set up a new username and password for authentication.

### - Product Management:
- Easily add new products by providing relevant details.
- Delete outdated or unnecessary products as required.
- View the entire product inventory in a structured format.

### - Sales Transactions:
- Conduct sales smoothly by selecting products and specifying quantities.
- Automatically update stock levels and track total sales.

### - Financial Monitoring:
- Check sales revenue and track financial growth over time.

### - Search Functionality:
- Quickly locate products using intuitive search queries.
- Review matching products for efficient inventory management.

### - User Navigation:
- Navigate through the system using the main menu options.
- Execute desired operations with straightforward command-line interactions.


