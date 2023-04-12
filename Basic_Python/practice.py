# # Yield from
# def yieldOnly():
#     yield "Sreekanth"
#     yield "Sourav"
#     yield "Satyamani"

# def yieldFrom():
#     for i in [1]:
#         yield from yieldOnly()
    
# test = yieldFrom()
# for i in test:
#     print(i)

# # lazy evaluation
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b , a + b

# fibonacci_Seq  = (n for i, n in enumerate(fibonacci()) if i < 10)

# for n in fibonacci_Seq:
#     print(n)

# # reading files using generators
# def pdf_reader(file_name):
#     for row in open (file_name, "r"):
#         yield row

# pdf_gen = pdf_reader("testfile.txt")
# row_count = 0 

# for row in pdf_gen:
#     row_count += 1

# print(f"Row count is {row_count}")
# pdf_gen = (row for row in open("testfile.txt"))   

# generator_methods
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def get_Even():
    value = 0 
    while True:
        if isEven(value):
            i = yield value
            if i is not None:
                value = i
        value += 1

even_gen = get_Even()
print(next(even_gen))
print(even_gen.send(1))
# it allows you to .send() a value back to the generator.
print(next(even_gen))

for x in even_gen:
    if x < 10:
        even_gen.throw(ValueError, "I, THINK IT WAS ENOUGH!")
        # .throw() allows you to throw exceptions with the generator.
        print(x)

for x in even_gen:
    if x > 10:
        even_gen.close() .close() 
        # .close() allows you to stop a generator. This can be especially handy when controlling an infinite sequence generator. 
    print(x)

# generator with context manager
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
for line in read_lines("testfile.txt"):
   print(line)
