import csv


def create_csv(file_path, columns, data):

    data = sorted(data, key=lambda x: (x[0], x[1]))

    # Open the file in write mode
    with open(file_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile, delimiter=';')

        # Write the column names
        writer.writerow(columns)

        # Write the data rows
        writer.writerows(data)

    print(f"CSV file '{file_path}' has been generated.")
