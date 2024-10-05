#=====importing libraries===========
# Import necessary libraries here, if required.
# In this case, we are not using any external libraries, but in the future,
# if you need to work with dates or other features, libraries like 'datetime' can be imported here.

#====Login Section====
# This section will allow a user to log in to the system by verifying their username and password.
# The usernames and passwords are stored in a 'user.txt' file in the format: username, password.
# The program will read from this file and use a while loop to repeatedly prompt the user
# until valid login credentials are entered.

# Open the 'user.txt' file to read the stored usernames and passwords.
with open("user.txt", "r") as user_file:
    # Create a dictionary to store the usernames and passwords.
    user_data = {}
    for line in user_file:
        username, password = line.strip().split(", ")
        user_data[username] = password

# Start a loop to prompt the user for login details.
while True:
    # Prompt the user to enter their username and password.
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    
    # Check if the entered username exists in the user_data dictionary.
    # If it does, verify if the corresponding password matches.
    if username_input in user_data and user_data[username_input] == password_input:
        print("Login successful!")
        break  # Exit the loop once the user logs in successfully.
    else:
        print("Invalid username or password. Please try again.")

# Main menu section that allows users to select various actions.
# The menu will be displayed after a successful login.
# Users can choose from options like registering a new user, adding a task, viewing all tasks, viewing their tasks, or exiting the program.
while True:
    # Present the menu to the user and convert the input to lowercase to ensure case insensitivity.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Option to register a new user.
    if menu == 'r':
        # Request input for the new username, password, and password confirmation.
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")

        # Check if the new password and confirmed password match.
        if new_password == confirm_password:
            # Append the new username and password to the 'user.txt' file.
            with open("user.txt", "a") as user_file:
                user_file.write(f"{new_username}, {new_password}\n")
            print("New user registered successfully.")
        else:
            print("Passwords do not match. Please try again.")

    # Option to add a new task to the task list.
    elif menu == 'a':
        # Gather the necessary details for the task from the user.
        task_user = input("Enter the username of the person assigned to the task: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter a description of the task: ")
        task_due_date = input("Enter the due date of the task (e.g., 2024-12-31): ")

        # You can add the current date dynamically using the datetime library, but here, we'll assume the date is entered manually.
        task_current_date = input("Enter the current date (e.g., 2024-10-05): ")

        # Append the task details to the 'task.txt' file.
        with open("task.txt", "a") as task_file:
            task_file.write(f"{task_user}, {task_title}, {task_description}, {task_current_date}, {task_due_date}, No\n")
        print("Task added successfully.")

    # Option to view all tasks.
    elif menu == 'va':
        # Open the 'task.txt' file and read all tasks.
        with open("task.txt", "r") as task_file:
            # For each task, split the line by ', ' and display the task in a readable format.
            for line in task_file:
                task_user, task_title, task_description, task_current_date, task_due_date, task_completed = line.strip().split(", ")
                print(f"Task assigned to: {task_user}")
                print(f"Title: {task_title}")
                print(f"Description: {task_description}")
                print(f"Date assigned: {task_current_date}")
                print(f"Due date: {task_due_date}")
                print(f"Completed: {task_completed}")
                print("-" * 50)

    # Option to view tasks assigned to the logged-in user.
    elif menu == 'vm':
        # Open the 'task.txt' file and read the tasks.
        with open("task.txt", "r") as task_file:
            # For each task, check if the username matches the logged-in user.
            for line in task_file:
                task_user, task_title, task_description, task_current_date, task_due_date, task_completed = line.strip().split(", ")
                if task_user == username_input:
                    # If the task belongs to the logged-in user, display it in a readable format.
                    print(f"Task assigned to: {task_user}")
                    print(f"Title: {task_title}")
                    print(f"Description: {task_description}")
                    print(f"Date assigned: {task_current_date}")
                    print(f"Due date: {task_due_date}")
                    print(f"Completed: {task_completed}")
                    print("-" * 50)

    # Option to exit the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()  # Terminates the program.

    # Handle invalid menu inputs.
    else:
        print("You have entered an invalid input. Please try again.")
