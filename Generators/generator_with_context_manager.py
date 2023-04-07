def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
for line in read_lines("testfile.txt"):
   print(line)
