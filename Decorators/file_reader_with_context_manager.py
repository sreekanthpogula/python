from contextlib import contextmanager

@contextmanager
def open_file(filename):
    try:
        f = open(filename, 'r')
        yield f
    finally:
        f.close()

def read_lines(filename):
    with open_file(filename) as f:
        for line in f:
            yield line.strip()

# Example usage
for line in read_lines('testfile.txt'):
    print(line)


