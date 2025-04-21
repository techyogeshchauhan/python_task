import csv
from typing import Dict, Any, Union

def find_highest_value_row(csv_file: str, column_name: str) -> Dict[str, Any]:
    """
    Find the row with the highest value in the specified column of a CSV file.
    
    Args:
        csv_file (str): Path to the CSV file
        column_name (str): Name of the column to find the highest value in
        
    Returns:
        Dict[str, Any]: The row with the highest value in the specified column
        
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        ValueError: If the column doesn't exist in the CSV file
    """
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            
            # Check if column exists
            if column_name not in reader.fieldnames:
                raise ValueError(f"Column '{column_name}' not found in CSV file")
            
            # Initialize variables
            highest_value = None
            highest_row = None
            
            # Iterate through rows
            for row in reader:
                try:
                    # Convert value to float if possible, otherwise keep as string
                    current_value = float(row[column_name])
                except ValueError:
                    current_value = row[column_name]
                
                # Update highest value and row if current value is higher
                if highest_value is None or current_value > highest_value:
                    highest_value = current_value
                    highest_row = row
            
            return highest_row
            
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file '{csv_file}' not found")

def main():
    # Example usage
    csv_file = "indian_employee_data.csv"
    
    try:
        # Find highest value in 'Score' column
        highest_row = find_highest_value_row(csv_file, "Score")
        print("\nRow with highest score:")
        for key, value in highest_row.items():
            print(f"{key}: {value}")
            
        # Find highest value in 'Age' column
        highest_row = find_highest_value_row(csv_file, "Age")
        print("\nRow with highest age:")
        for key, value in highest_row.items():
            print(f"{key}: {value}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 