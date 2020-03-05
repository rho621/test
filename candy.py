candy_cart = ["snickers", "kit kat", "coffee candy", "gummy bear", "cookies"]

"""
for candy in candy_cart:
    print(candy_cart.index(candy))
"""

for candy in candy_cart:
    print("[" + str(candy_cart.index(candy)) + "] " + candy)

allowance = 3
cart = []
for count in range(allowance):

    candy_choice = int(input("Enter candy number: " ))
    cart.append(candy_cart[candy_choice])

print(cart)

