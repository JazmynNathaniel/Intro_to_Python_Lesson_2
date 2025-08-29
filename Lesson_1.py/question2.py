print("Welcome to Bob's burgrs!")
print("Please enter your name")
name = input()
print("Hello " + name + "!")
print("Please select the Items you would like to order:")
print("1. Burger - $5")
print("2. Fries - $3")
input_item = int(input())
print("Would you like to add a drink? (yes/no)")
drink = input().lower()
if drink == "yes":
    print("3. Drink - $2")
    drink_price = 2
else:
    drink_price = 0
    print("No drink added.")
    print("You can add a drink later if you change your mind.")
print("Your order summary:")
print(f"Your Order Total is: ${input_item + drink_price}")
print("Thank you for your order, " + name + "! Enjoy your meal!")
