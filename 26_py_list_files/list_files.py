import os
from datetime import datetime

def list_directory_contents(path='.'):
    """
    Lists all files and directories in the specified path with detailed information.
    
    Args:
        path (str): The path to list contents from. Defaults to current directory.
    """
    try:
        # Get the absolute path
        abs_path = os.path.abspath(path)
        print(f"\nContents of directory: {abs_path}\n")
        print("Type\tSize (bytes)\tLast Modified\t\tName")
        print("-" * 80)
        
        # List all entries in the directory
        for entry in os.listdir(path):
            # Get the full path of the entry
            full_path = os.path.join(path, entry)
            
            # Get file/directory information
            if os.path.isdir(full_path):
                entry_type = "DIR"
                size = "-"
            else:
                entry_type = "FILE"
                size = os.path.getsize(full_path)
            
            # Get last modified time
            modified_time = os.path.getmtime(full_path)
            modified_date = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
            
            # Print the entry information
            print(f"{entry_type}\t{size}\t{modified_date}\t{entry}")
            
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("Directory Listing Tool")
    print("=" * 50)
    
    while True:
        # Get user input for the directory path
        user_path = input("\nEnter the directory path (press Enter for current directory, 'q' to quit): ").strip()
        
        # Check if user wants to quit
        if user_path.lower() == 'q':
            print("Goodbye!")
            break
        
        # If user didn't enter anything, use current directory
        if not user_path:
            user_path = '.'
        
        # List the directory contents
        list_directory_contents(user_path)

if __name__ == "__main__":
    main() 