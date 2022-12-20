# stack follows LIFO order, used when data is sequential
# Stack operations are push, pop
# we can implement stack using list, deque and queue.LifoQueue Class

# class Stack:
#     def __init__(self):
#         self.items = []


# def is_empty(self):
#     return self.items == []

#     def push(self, data):
#         self.items.append(data)

#     def pop(self):
#         return self.items.pop()


# s = Stack()
# while True:
#     print('push<value>')
#     print('pop')
#     print('quit')
# do = input('what would you like to do?').split()
# operation = do[0].strip().lower()
# if operation == 'push':
#     s.push(int(do[1]))
# elif operation == 'pop':
#     if s.is_empty():
#         print('empty')
#     else:
#         print('popped value:', s.pop())
# elif operation == 'quit':
#     print('finished')

# using list Built-in
from queue import LifoQueue
# from collections import deque
# s = []
# s.append('eat')
# s.append('sleep')
# s.append('code')
# print(s)
# s.pop()
# s.pop()
# s.pop()

# # The collections.deque Class
# q = deque
# q.append('eat')
# q.append('sleep')
# q.append('code')
# q.pop()
# q.pop()


# queue.LifoQueue Class
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
s.get()
s.get_nowait()
s.get()
