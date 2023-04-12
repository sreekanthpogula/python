def adjacent_boxes(coord):
    row, col = coord
    if row > 8 or col > 8:
        raise ValueError("Error: Coordinates must be between 1 and 8.")
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue  
            if 1 <= r <= 8 and 1 <= c <= 8:
                yield (r, c)
            
user_input = input('Enter space-separated integer coordinates: ')
my_tuple = tuple(int(item) for item in user_input.split())
try:
    for box in adjacent_boxes((my_tuple)):
        print(box)
except ValueError as e:
    print(e)