# User-defined function to calculate total amount
def calculate_total_amount(apple_quantity, orange_quantity, apple_price, orange_price):
    # Calculate total amount
    total_amount = (apple_quantity * apple_price) + (orange_quantity * orange_price)

    return total_amount

# User-defined function to display receipt
def display_receipt(apple_quantity, orange_quantity, apple_price, orange_price, total_amount):
    print("\n********** Receipt **********")
    print(f"Quantity of apples: {apple_quantity}")
    print(f"Unit price of apples: {apple_price} pesos")
    print(f"Subtotal for apples: {apple_quantity * apple_price} pesos")

    print(f"\nQuantity of oranges: {orange_quantity}")
    print(f"Unit price of oranges: {orange_price} pesos")
    print(f"Subtotal for oranges: {orange_quantity * orange_price} pesos")

    print("\n*****************************")
    print(f"Total amount to be paid: {total_amount} pesos")
    print("*****************************")

# Main program
if __name__ == "__main__":
    # Prices of apples and oranges in pesos
    apple_price = 20
    orange_price = 25

    # Get user input for the number of apples and oranges
    apple_quantity = int(input("Enter the quantity of apples you want to buy: "))
    orange_quantity = int(input("Enter the quantity of oranges you want to buy: "))

    # Calculate the total amount using the user-defined function
    total_amount = calculate_total_amount(apple_quantity, orange_quantity, apple_price, orange_price)

    # Display the receipt using the user-defined function
    display_receipt(apple_quantity, orange_quantity, apple_price, orange_price, total_amount)

    # Keep the console window open
    input("Press Enter to exit...")

