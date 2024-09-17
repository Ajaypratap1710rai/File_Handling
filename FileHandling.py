import csv
import os

def check_and_create_csv(file_path, headers):
    """Check if the CSV file exists, and create it if it does not."""
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f"{file_path} created with headers: {headers}")
    else:
        print(f"{file_path} already exists.")

def write_record(file_path, record):
    """Write a new record to the CSV file."""
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(record)
    print(f"Record {record} added to {file_path}.")

def update_record(file_path, old_record, new_record):
    """Update a record in the CSV file."""
    updated = False
    rows = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Update the record
    for i, row in enumerate(rows):
        if row == old_record:
            rows[i] = new_record
            updated = True
            break

    if updated:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Record {old_record} updated to {new_record} in {file_path}.")
    else:
        print(f"Record {old_record} not found in {file_path}.")

def delete_record(file_path, record):
    """Delete a record from the CSV file."""
    rows = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row != record]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Record {record} deleted from {file_path}.")

def main():
    """Main function to interact with the user and perform operations."""
    csv_file_path = input("Enter the path to the CSV file: ").strip()

    if not os.path.exists(csv_file_path):
        headers = input("Enter the headers for the CSV file (comma-separated): ").strip().split(',')
        headers = [header.strip() for header in headers]  # Clean up any extra spaces
        check_and_create_csv(csv_file_path, headers)
    else:
        # Load headers from existing file
        with open(csv_file_path, mode='r', newline='') as file:
            headers = next(csv.reader(file))

    while True:
        operation = input("Choose operation: write, update, delete, or exit: ").strip().lower()

        if operation == 'write':
            record = input("Enter the record to write (comma-separated): ").strip().split(',')
            record = [field.strip() for field in record]  # Clean up any extra spaces
            if len(record) == len(headers):
                write_record(csv_file_path, record)
            else:
                print("Error: Record length does not match headers length.")
        elif operation == 'update':
            old_record = input("Enter the old record to update (comma-separated): ").strip().split(',')
            new_record = input("Enter the new record (comma-separated): ").strip().split(',')
            old_record = [field.strip() for field in old_record]
            new_record = [field.strip() for field in new_record]
            if len(new_record) == len(headers):
                update_record(csv_file_path, old_record, new_record)
            else:
                print("Error: New record length does not match headers length.")
        elif operation == 'delete':
            record = input("Enter the record to delete (comma-separated): ").strip().split(',')
            record = [field.strip() for field in record]
            if len(record) == len(headers):
                delete_record(csv_file_path, record)
            else:
                print("Error: Record length does not match headers length.")
        elif operation == 'exit':
            print("Exiting.")
            break
        else:
            print("Invalid operation. Please choose 'write', 'update', 'delete', or 'exit'.")

if __name__ == "__main__":
    main()
