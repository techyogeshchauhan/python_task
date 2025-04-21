import requests
from typing import List, Dict, Any
import json
from datetime import datetime

def fetch_users(api_url: str = "https://jsonplaceholder.typicode.com/users") -> List[Dict[str, Any]]:
    """
    Fetch user data from the specified API endpoint.
    
    Args:
        api_url (str): The URL of the API endpoint
        
    Returns:
        List[Dict[str, Any]]: List of user data dictionaries
        
    Raises:
        requests.exceptions.RequestException: If there's an error with the API request
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []

def display_users(users: List[Dict[str, Any]]) -> None:
    """
    Display user information in a formatted way.
    
    Args:
        users (List[Dict[str, Any]]): List of user data dictionaries
    """
    if not users:
        print("No users found.")
        return
    
    print("\n=== User List ===")
    print(f"Total Users: {len(users)}")
    print("=" * 50)
    
    for i, user in enumerate(users, 1):
        print(f"\nUser #{i}")
        print(f"Name: {user.get('name', 'N/A')}")
        print(f"Username: {user.get('username', 'N/A')}")
        print(f"Email: {user.get('email', 'N/A')}")
        print(f"Phone: {user.get('phone', 'N/A')}")
        print(f"Website: {user.get('website', 'N/A')}")
        print("-" * 50)

def save_users_to_file(users: List[Dict[str, Any]], filename: str = "users_data.json") -> None:
    """
    Save user data to a JSON file.
    
    Args:
        users (List[Dict[str, Any]]): List of user data dictionaries
        filename (str): Name of the file to save the data to
    """
    try:
        with open(filename, 'w') as f:
            json.dump(users, f, indent=4)
        print(f"\nUser data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

def main():
    print("Fetching user data from API...")
    users = fetch_users()
    
    if users:
        display_users(users)
        save_users_to_file(users)
    else:
        print("Failed to fetch user data.")

if __name__ == "__main__":
    main() 