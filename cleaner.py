import csv
import os

file_path = os.path.join("..", "Resources", "cereal.csv")

print(file_path)

with open(file_path, 'r') as file_handle:
    csv_handle = csv.reader(file_handle, delimiter=',')

    header = next(csv_handle)
    for line in csv_handle:
        if(float(line[7]) > 5):
            print(line)