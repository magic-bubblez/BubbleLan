from lexer import Tokenizer, INTEGER, IDENT, ASSIGN, PLUS, MULTIPLY, DIVIDE, MINUS, SAY, EOF, GRT, LST, STRING, IF, THEN, ELSE, EQ, NEQ, FOR, IN, FROM, TO, COLON, LBRACKET, RBRACKET, COMMA
from my_ast import Num, BinOp, Var, Assign, Say, String, If, Array, For, Range, Index

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.curr_token.type == token_type:
            self.curr_token = self.lexer.get_next_token()
        else:
            raise Exception(f'Expected {token_type}, got {self.curr_token.type}')

    def factor(self):
        token = self.curr_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token.value)
        elif token.type == STRING:
            self.eat(STRING)
            return String(token.value)
        elif token.type == LBRACKET:
            return self.list_literal()
        elif token.type == IDENT:
            name = token.value
            self.eat(IDENT)

            if self.curr_token.type == LBRACKET:
                self.eat(LBRACKET)
                index = self.expr()
                self.eat(RBRACKET)
                return Index(Var(name), index)
            return Var(name)

    def list_literal(self):
        self.eat(LBRACKET)
        elements = []
        if self.curr_token.type != RBRACKET:
            elements.append(self.expr())
            while self.curr_token.type == COMMA:
                self.eat(COMMA)
                elements.append(self.expr())
        self.eat(RBRACKET)
        return Array(elements)

    def term(self):
        node = self.factor()
        while self.curr_token.type in (MULTIPLY, DIVIDE):
            op = self.curr_token.value
            if self.curr_token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif self.curr_token.type == DIVIDE:
                self.eat(DIVIDE)
            node = BinOp(node, op, self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.curr_token.type in (PLUS, MINUS):
            op = self.curr_token.value
            if self.curr_token.type == PLUS:
                self.eat(PLUS)
            elif self.curr_token.type == MINUS:
                self.eat(MINUS)
            node = BinOp(node, op, self.term())
        return node
    
    def comparison(self):
        node = self.expr()
        if self.curr_token.type in (EQ, NEQ, LST, GRT):
            op = self.curr_token.value
            token_type = self.curr_token.type
            self.eat(token_type)
            node = BinOp(node, op, self.expr())
        return node

    def assign_stmt(self):
        var_name = self.curr_token.value
        self.eat(IDENT)
        self.eat(ASSIGN)
        value = self.expr()
        return Assign(var_name, value)

    def say_stmt(self):
        self.eat(SAY)
        expr = self.expr()
        return Say(expr)
    
    def if_stmt(self):
        self.eat(IF)
        condition = self.comparison()
        self.eat(THEN)
        then_branch = self.statement()
        else_branch = None
        if self.curr_token.type == ELSE:
            self.eat(ELSE)
            else_branch = self.statement()
        return If(condition, then_branch, else_branch)

    def for_stmt(self):
        self.eat(FOR)
        var_name = self.curr_token.value
        self.eat(IDENT)
        
        # Two syntaxes: "for i in list:" or "for i from start to end:"
        if self.curr_token.type == IN:
            self.eat(IN)
            iterable = self.expr()
        elif self.curr_token.type == FROM:
            self.eat(FROM)
            start = self.expr()
            self.eat(TO)
            end = self.expr()
            iterable = Range(start, end)
        else:
            raise Exception(f'Expected IN or FROM after for variable')
        
        self.eat(COLON)
        
        # Collect body statements (one statement for now)
        body = [self.statement()]
        
        return For(var_name, iterable, body)

    def statement(self):
        if self.curr_token.type == IDENT:
            return self.assign_stmt()
        elif self.curr_token.type == SAY:
            return self.say_stmt()
        elif self.curr_token.type == IF:
            return self.if_stmt()
        elif self.curr_token.type == FOR:
            return self.for_stmt()
        else:
            raise Exception(f'Unexpected token {self.curr_token.type} in statement')

    def program(self):
        statements = []
        while self.curr_token.type != EOF:
            statements.append(self.statement())
        return statements  # list of AST nodes
