class Num:
    def __init__(self, value): self.value = value 

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class String:
    def __init__(self, value): self.value = value

class Var:
    def __init__(self, name): self.name = name

class Assign:
    def __init__(self, name, value):
        self.name, self.value = name, value 

class Say:
    def __init__(self, expr): self.expr = expr

class If:
    def __init__(self, condition, then_branch, else_branch):
        self.condition, self.then_branch, self.else_branch = condition, then_branch, else_branch

class Array:
    def __init__(self, elements): self.elements = elements

class For:
    def __init__(self, var, iterable, body):
        self.var = var          
        self.iterable = iterable
        self.body = body

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Index:
    def __init__(self, array, index):
        self.array = array
        self.index = index

class Dictionary:
    def __init__(self, pairs): self.pairs = pairs



