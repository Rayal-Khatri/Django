import random
import csv

def generate_random_row(x):
    x = [int(item) for item in x.split()]

    ones_indices = [i for i, value in enumerate(x) if value == 1]
    zeros_indices = [i for i, value in enumerate(x) if value == 0]

    random.shuffle(ones_indices)
    random.shuffle(zeros_indices)

    for i in range(4):
        x[ones_indices[i]] = 0

    for i in range(20):
        x[zeros_indices[i]] = 1

    return x

def write_to_csv(rows):
    with open('new_dataset.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows)

def main():
    first_item = ''
    for _ in range(100):
        temp = ["Ear Mites"] + generate_random_row(first_item)
        write_to_csv(temp)

if __name__ == "__main__":
    main()
