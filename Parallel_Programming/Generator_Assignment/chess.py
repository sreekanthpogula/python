def adjacent_boxes(coord):
    row, col = coord
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue  
            if 1 <= r <= 8 and 1 <= c <= 8:
                yield (r, c) 

for box in adjacent_boxes((2,2)):
    print(box)