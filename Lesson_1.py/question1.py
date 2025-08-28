print("Welcome to the Movie Theater!")
print("Please enter your name")
name = input()
print("Hello " + name + "!")
print("how many tickets would you like to purchase?")
tickets = int(input())
print("Please select the type of ticket you would like to purchase:")
print("1. Adult - $12")
print("2. Child - $8")
print("3. Senior - $10")
ticket_type = int(input())
if ticket_type == 1:
    price = 12
elif ticket_type == 2:
    price = 8
elif ticket_type == 3:
    price = 10
else:
    print("Invalid ticket type selected. Please restart the program.")
    exit()
total_cost = tickets * price
print(f"The total cost of " + str(tickets) +
      " tickets is: $" + str(total_cost))
print("Thank you for your purchase, " + name + "! Enjoy the movie!")
