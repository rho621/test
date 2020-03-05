print("Welcome to the House of Pies")

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

for pies in pie_list:
    print("[" + str(pie_list.index(pies)) + "] " + pies)

cart = []

ask = "yes"

while ask == "yes":
    
    pie_choice = int(input("What kind of pies would you like? "))
    cart.append(pie_list[pie_choice])

    ask = input("Would you like to order another one? ")

print("You purchaced:")
for items in cart:
    print(str(pie_list.index(pies)) + " " + cart)
