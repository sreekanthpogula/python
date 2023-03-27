# Define a decorator function that takes a function as input
def login_required(func):
    # Define a new function that wraps the original function
    def wrapper(*args, **kwargs):
        # Check if the user is logged in
        if user_is_logged_in():
            # If the user is logged in, call the original function
            return func(*args, **kwargs)
        else:
            # If the user is not logged in, raise an exception or redirect to login page
            raise Exception("User not logged in")
    # Return the new function
    return wrapper

# Define a function that requires login
@login_required
def do_something_secure():
    # This function can only be called if the user is logged in
    pass

def delete_account(user_id):
    if current_user_id() == user_id:
        delete_user_account(user_id)
    else:
        raise Exception("You can only delete your own account")
    
# Define a global variable to store the current user ID
current_user = None

# Define a function to log in a user
def login(user_id):
    global current_user
    current_user = user_id

# Define a function to log out the current user
def logout():
    global current_user
    current_user = None

# Define a function to check if the user is logged in
def user_is_logged_in():
    global current_user
    return current_user is not None

# Define a function to get the ID of the currently logged in user
def current_user_id():
    global current_user
    return current_user

# Define a function to delete a user account
def delete_user_account(user_id):
    global current_user
    if current_user == user_id:
        print(f"Deleting user account with ID {user_id}")
        current_user = None
    else:
        raise Exception("You can only delete your own account")

# Define the login_required decorator
def login_required(func):
    def wrapper(*args, **kwargs):
        if user_is_logged_in():
            return func(*args, **kwargs)
        else:
            raise Exception("User not logged in")
    return wrapper

# Define a function that requires login
@login_required
def delete_account(user_id):
    if current_user_id() == user_id:
        delete_user_account(user_id)
    else:
        raise Exception("You can only delete your own account")

# Test the delete_account function
login(1070)
delete_account(1070)  # Should print "Deleting user account with ID 1"
logout()

try:
    delete_account(1070)  # Should raise an exception
except Exception as e:
    print(e)

login(1070)

try:
    delete_account(1)  # Should raise an exception
except Exception as e:
    print(e)

delete_account(1070)  # Should print "Deleting user account with ID 2"
logout()
login(1070)
print(current_user_id())

