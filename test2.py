x = 90
y = 15

if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")
else:
    if y < 5:
        print("x is greater than or equal to 10 and y is less than 5")
    elif y == 5:
        print("x is greater than or equal to  than 10 and y is equal to 5")
    else:
        print("x is greater than or equal to  than 10 and y is greater than 5")

