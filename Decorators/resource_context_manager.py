class contextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with contextManager() as manager:
    print('with statement block')