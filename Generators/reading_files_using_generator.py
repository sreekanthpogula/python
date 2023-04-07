def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
csv_gen = csv_reader("testfile.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

# csv_gen = (row for row in open("testfile.txt"))
