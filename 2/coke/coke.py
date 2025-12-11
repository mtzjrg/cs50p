# Coke Machine: Implement a program that prompts the user to insert a coin, one
#               at a time, each informing the user of the amount due. Once the
#               user has inputted at least 50 cents, output how many cents in
#               change the user is owed.
#
#               Assume the user will only input integers, and ignore any integer
#               that isn't an accepted denomination.

amount_due = 50

while True:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        amount_due -= coin

    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
        break
