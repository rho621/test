def avg(arg1):
    count = len(arg1)
    sum = 0

    for item in arg1:
        sum = sum + item 
    result = sum/count
    return result

input_1 = [1,2,3]
input_2 = [7, 8, 9, 10, 11]

print(avg(input_1))
print(avg(input_2))