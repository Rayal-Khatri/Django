import csv

def find_duplicate_rows(filename):
    row_number_dict = {}
    duplicate_rows = []

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row_number, row in enumerate(reader, start=1):
            row_tuple = tuple(row)
            if row_tuple in row_number_dict:
                duplicate_rows.append((row_number_dict[row_tuple], row_number))
            else:
                row_number_dict[row_tuple] = row_number

    return duplicate_rows

def main():
    filename = 'new_dataset.csv'  # Change this to the name of your CSV file

    duplicate_rows = find_duplicate_rows(filename)
    if not duplicate_rows:
        print("No duplicate rows found.")
    else:
        print("Duplicate rows found at the following row numbers:")
        for duplicate_row in duplicate_rows:
            print(f"Row {duplicate_row[0]} and Row {duplicate_row[1]}")

if __name__ == "__main__":
    main()
