def main():
    # Initialize an empty dictionary to store product names and prices
    products = {}

    # Keep taking input from the user until they say 'n' or 'no'
    while True:
        # Ask the user to enter product name and price
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))

        # Store the product name and price in the dictionary
        products[product_name] = price

        # Ask the user if they want to enter more products
        choice = input("Do you want to enter more products? (y/n): ")
        if choice.lower() in ('n', 'no'):
            break

    # Allow the user to search for a product by name
    search_product = input("Enter a product name to get its price: ")
    if search_product in products:
        print(f"The price of {search_product} is ${products[search_product]:.2f}")
    else:
        print("Product not found.")

    # Allow the user to enter a price range and print products within that range
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    print(f"Products within price range ${min_price:.2f} - ${max_price:.2f}:")
    for product, price in products.items():
        if min_price <= price <= max_price:
            print(f"{product}: ${price:.2f}")


if __name__ == "__main__":
    main()
