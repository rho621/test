print("Welcome to the House of Pies")

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

count_of_pies = len(pie_list)

string_of_choice = ""

for i in range(count_of_pies):
    string_of_choice = string_of_choice + ("[" + str(i +1) + "] ") +(pie_list[i] + ", ")

string_of_choice = string_of_choice.strip(", ")

print(string_of_choice)

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ask = "yes"

while ask == "yes":
    choice = int(input("Pick your pie: "))
    count[choice -1] = count[choice - 1] + 1

    ask = input("Would you like to order another one? ")

for i in range(count_of_pies):
    print((str(count[i]) + " " + pie_list[i]))
