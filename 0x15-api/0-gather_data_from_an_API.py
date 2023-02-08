#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import sys
import requests

# Define the API endpoints
USERS_API = "https://jsonplaceholder.typicode.com/users"
TODOS_API = "https://jsonplaceholder.typicode.com/todos"

# Function to retrieve the employee's name
def get_employee_name(employee_id):
    # Get all the users
    response = requests.get(USERS_API)
    users = response.json()
    
    # Find the employee with the given ID
    employee = [user for user in users if user["id"] == employee_id]
    
    return employee[0]["name"]

# Function to retrieve the employee's TODO list
def get_employee_todos(employee_id):
    # Get all the TODOs
    response = requests.get(TODOS_API)
    todos = response.json()
    
    # Filter the TODOs by employee ID
    employee_todos = [todo for todo in todos if todo["userId"] == employee_id]
    
    return employee_todos

# Main function
if __name__ == "__main__":
    # Get the employee ID from the command line argument
    employee_id = int(sys.argv[1])
    
    # Get the employee name
    employee_name = get_employee_name(employee_id)
    
    # Get the employee's TODO list
    employee_todos = get_employee_todos(employee_id)
    
    # Get the count of completed and total TODOs
    total = len(employee_todos)
    completed = len([todo for todo in employee_todos if todo["completed"]])
    
    # Display the result in the required format
    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for todo in employee_todos:
        if todo["completed"]:
            print(f"\t {todo['title']}")

