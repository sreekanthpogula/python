# magic method in python
class String:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return self.string


if __name__ == '__main__':
    string1 = String('Hello')
    print(string1)
