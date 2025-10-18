# lexer.py
INTEGER, IDENT, ASSIGN, PLUS, MULTIPLY, DIVIDE, MINUS, SAY, EOF, GRT, LST, STRING, IF, THEN, ELSE, EQ, NEQ, FOR, IN, FROM, TO, COLON, LBRACKET, RBRACKET, COMMA = 'INTEGER', 'IDENT', 'ASSIGN', 'PLUS', 'MULTIPLY', 'DIVIDE', 'MINUS', 'SAY', 'EOF', 'GRT', 'LST', 'STRING', 'IF', 'THEN', 'ELSE', 'EQ', 'NEQ', 'FOR', 'IN', 'FROM', 'TO', 'COLON', 'LBRACKET', 'RBRACKET', 'COMMA'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Tokenizer:
    def __init__(self, txt):
        self.txt = txt
        self.pos = 0
        self.curr_char = txt[self.pos] if txt else None

    def pointer(self):
        self.pos += 1
        self.curr_char = self.txt[self.pos] if self.pos < len(self.txt) else None

    def skip_whitespace(self):
        while self.curr_char and self.curr_char.isspace():
            self.pointer()


    def number(self):
        result = ''
        while self.curr_char and self.curr_char.isdigit():
            result += self.curr_char
            self.pointer()
        return int(result)

    def string(self):
        result = ''
        self.pointer() 
        while self.curr_char and self.curr_char != '"':
            result += self.curr_char
            self.pointer()
        if self.curr_char == '"':
            self.pointer() # skip closing quote
        return result

    def identifier(self):
        result = ''
        while self.curr_char and self.curr_char.isalnum():
            result += self.curr_char
            self.pointer()
        if result == 'say':
            return Token(SAY, result)
        if result == 'if':
            return Token(IF, result)
        if result == 'then':
            return Token(THEN, result)
        if result == 'else':
            return Token(ELSE, result)
        if result == 'for':
            return Token(FOR, result)
        if result == 'in':
            return Token(IN, result)
        if result == 'from':
            return Token(FROM, result)
        if result == 'to':
            return Token(TO, result)
        return Token(IDENT, result)

    def get_next_token(self):
        while self.curr_char:
            if self.curr_char.isspace():
                self.skip_whitespace()
                continue
            if self.curr_char.isdigit():
                return Token(INTEGER, self.number())
            if self.curr_char.isalpha():
                return self.identifier()
            
            if self.curr_char == '=':
                self.pointer()
                if self.curr_char == '=':  
                    self.pointer()
                    return Token(EQ, '==')
                return Token(ASSIGN, '=')
            
            if self.curr_char == '!':
                self.pointer()
                if self.curr_char == '=':
                    self.pointer()
                    return Token(NEQ, '!=')
                raise Exception(f'Unknown character: !')
            if self.curr_char == '<':
                self.pointer()
                return Token(LST, '<')
            if self.curr_char == '>':
                self.pointer()
                return Token(GRT, '>')
            if self.curr_char == '+':
                self.pointer()
                return Token(PLUS, '+')
            if self.curr_char == '-':
                self.pointer()
                return Token(MINUS, '-')
            if self.curr_char == '*':   
                self.pointer()
                return Token(MULTIPLY, '*')
            if self.curr_char == '/':
                self.pointer()
                return Token(DIVIDE, '/')
            if self.curr_char == '"':
                return Token(STRING, self.string())
            if self.curr_char == ':':
                self.pointer()
                return Token(COLON, ':')
            if self.curr_char == '[':
                self.pointer()
                return Token(LBRACKET, '[')
            if self.curr_char == ']':
                self.pointer()
                return Token(RBRACKET, ']')
            if self.curr_char == ',':
                self.pointer()
                return Token(COMMA, ',')
            raise Exception(f'Unknown character: {self.curr_char}')
        return Token(EOF, None)
