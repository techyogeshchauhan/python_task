import random
import csv

# Lists of Indian names and departments
first_names = ['Aarav', 'Priya', 'Vikram', 'Ananya', 'Rohan', 'Isha', 'Arjun', 'Kavya', 'Siddharth', 'Neha', 'Aditya', 'Meera', 'Rahul', 'Pooja', 'Amit', 'Shreya', 'Karan', 'Riya', 'Vivek', 'Sneha']
last_names = ['Sharma', 'Patel', 'Singh', 'Gupta', 'Mehta', 'Verma', 'Rao', 'Nair', 'Joshi', 'Kapoor', 'Reddy', 'Kumar', 'Chopra', 'Malhotra', 'Bose']
departments = ['Engineering', 'Marketing', 'Finance', 'HR', 'IT']

# Generate 500 entries
data = []
for _ in range(500):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(22, 50)
    score = round(random.uniform(70.0, 100.0), 1)
    dept = random.choice(departments)
    data.append([name, age, score, dept])

# Write to CSV
with open('indian_employee_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Score', 'Department'])
    writer.writerows(data)

print("CSV file 'indian_employee_data.csv' generated with 500 entries.")