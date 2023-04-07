# Define a dictionary of users with their roles
USERS = {
    'alice': 'admin',
    'bob': 'user',
    'charlie': 'user',
}

# Define a decorator to restrict access based on role
def access_control(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if USERS.get('current_user') == role:
                return func(*args, **kwargs)
            else:
                raise ValueError('Access denied')
        return wrapper
    return decorator

# Define a function that requires admin access
@access_control('admin')
def admin_function():
    print('This is an admin function')

# Define a function that requires user access
@access_control('user')
def user_function():
    print('This is a user function')

# Simulate a user logging in with admin access
USERS['current_user'] = 'alice'

# Call the functions with appropriate access levels
try:
    admin_function()  # This is an admin function
    # user_function()  # Access denied
except ValueError as e:
    print(e)

# Simulate a user logging in with user access
USERS['current_user'] = 'bob'

# Call the functions with appropriate access levels
try:
    # admin_function()  # Access denied
    user_function()  # This is a user function
except ValueError as e:
    print(e)


