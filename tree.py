# tree
class node:
    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None


def pre_order(self):
    if self:
        print(self.parent)
        pre_order(self.left)
        pre_order(self.right)


n = node('first')
n.left = node('second')
n.right = node('third')
pre_order(n)
