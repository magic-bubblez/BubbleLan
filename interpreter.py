from my_ast import Num, BinOp, Var, Assign, Say, String, If, Array, For, Range, Index

class Interpreter:
    def __init__(self):
        self.env = {}

    def goto(self, node):
        method_name = 'goto' + type(node).__name__
        return getattr(self, method_name)(node)

    def gotoNum(self, node):
        return node.value

    def gotoVar(self, node):
        return self.env[node.name]

    def gotoString(self, node):
        return node.value

    def gotoBinOp(self, node):
        left = self.goto(node.left)
        right = self.goto(node.right)
        if node.op == '+':
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            return left / right
        elif node.op == '==':
            return left == right
        elif node.op == '!=':
            return left != right
        elif node.op == '<':
            return left < right
        elif node.op == '>':
            return left > right
        else:
            raise Exception(f'Unknown operator: {node.op}')

    def gotoAssign(self, node):
        self.env[node.name] = self.goto(node.value)

    def gotoSay(self, node):
        print(self.goto(node.expr))
    
    def gotoIf(self, node):
        condition = self.goto(node.condition)
        if condition:
            return self.goto(node.then_branch)
        elif node.else_branch is not None:
            return self.goto(node.else_branch)

    def gotoArray(self, node):
        return [self.goto(elem) for elem in node.elements]
    
    def gotoRange(self, node):
        start = self.goto(node.start)
        end = self.goto(node.end)
        return list(range(start, end + 1))  # inclusive range
    
    def gotoIndex(self, node):
        array = self.goto(node.array)
        index = self.goto(node.index)
        return array[index]
    
    def gotoFor(self, node):
        iterable = self.goto(node.iterable)
        for value in iterable:
            
            self.env[node.var] = value
            # Execute body
            for stmt in node.body:
                self.goto(stmt)
