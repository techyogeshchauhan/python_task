import csv
import os
from typing import List, Dict, Union

def append_to_csv(data: Union[List[Dict], List[List]], file_path: str) -> None:
    """
    Append data to a CSV file. Creates the file if it doesn't exist.
    
    Args:
        data: List of dictionaries or list of lists containing the data to write
        file_path: Path to the CSV file
    
    Raises:
        ValueError: If data format is invalid
        IOError: If there are file operation issues
    """
    if not data:
        raise ValueError("Data cannot be empty")
    
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.exists(file_path)
    
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            # Determine if data is list of dictionaries or list of lists
            if isinstance(data[0], dict):
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerows(data)
            else:
                writer = csv.writer(file)
                if not file_exists:
                    # If it's a list of lists, write the first row as header
                    writer.writerow([f"Column_{i+1}" for i in range(len(data[0]))])
                writer.writerows(data)
    except Exception as e:
        raise IOError(f"Error writing to CSV file: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example with dictionary data
    dict_data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "London"}
    ]
    
    # Example with list data
    list_data = [
        ["John", 30, "New York"],
        ["Alice", 25, "London"]
    ]
    
    # Try both examples
    try:
        append_to_csv(dict_data, "example_dict.csv")
        print("Successfully wrote dictionary data to CSV")
        
        append_to_csv(list_data, "example_list.csv")
        print("Successfully wrote list data to CSV")
    except Exception as e:
        print(f"Error: {str(e)}")

# For dictionary data
data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
append_to_csv(data, "output.csv")

# For list data
data = [["John", 30], ["Alice", 25]]
append_to_csv(data, "output.csv") 