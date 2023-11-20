def calculate_max_apples(money, apple_price):
    # Calculate the maximum number of apples
    max_apples = money // apple_price
    
    # Calculate the remaining money after buying apples
    remaining_money = money % apple_price
    
    return max_apples, remaining_money

def display_results(max_apples, remaining_money):
    # Display the results
    print("\nMaximum number of apples you can buy: ", max_apples)
    print("Remaining money: ${:.2f}".format(remaining_money))

def main():
    # Get user input for the amount of money and the price of an apple
    money = float(input("Enter the amount of money you have: $"))
    apple_price = float(input("Enter the price of an apple: $"))

    # Call the user-defined function to calculate the maximum number of apples and remaining money
    max_apples, remaining_money = calculate_max_apples(money, apple_price)

    # Display the results
    display_results(max_apples, remaining_money)

    # Additional feature: Calculate and display the average cost per apple
    if max_apples > 0:
        average_cost_per_apple = money / max_apples
        print("Average cost per apple: ${:.2f}".format(average_cost_per_apple))
    else:
        print("You cannot buy any apples with the given amount.")

if __name__ == "__main__":
    main()
