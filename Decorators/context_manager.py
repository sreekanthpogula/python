# A context manager is an object that defines the methods __enter__ and __exit__. The __enter__ method is called when the context manager is entered, and the __exit__ method is called when the context manager is exited. The with statement is used to enter and exit the context manager.

# Here's an example of how to create a context manager using the contextlib.contextmanager decorator:

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # code to enter the context
    print("Entering the context")
    yield
    # code to exit the context
    print("Exiting the context")

#using the context manager
with my_context_manager():
    print("Inside the context")
