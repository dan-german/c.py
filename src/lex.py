from enum import Enum
import utils

operators = { "*", "+", "=" }
types = { "int" }

class TokenType(Enum): 
    ID = 1
    OPERATOR = 2
    INT_LITERAL = 3
    TYPE = 4
    EOS = 5 

class Token: 
    def __eq__(self, other): 
        return self.type == other.type and self.value == other.value
    def __init__(self, *, type: TokenType = None, value: str = None): 
        self.type = type
        self.value = value
    def __repr__(self): 
        return f"{self.type.name}" + (f" {self.value}" if self.value else "")

class Tokens: 
    def __init__(self, file_string: str): 
        self.tokens: list[Token] = []
        self.run(file_string)
    def __len__(self): return len(self.tokens)
    def __getitem__(self, i): return self.tokens[i]
    def __eq__(self, other): return self.tokens == other.tokens
    def __iadd__(self, token: Token):
        self.tokens.append(token)
        return self
    def __repr__(self): 
        res = ""
        for i, token in enumerate(self.tokens): 
            res += str(i) + " " + token.__repr__()
            if i < len(self.tokens) - 1: res += "\n"
        return res
    def __iter__(self): 
        return iter(self.tokens)
    def run(self, file_string: str): 
        peeker = utils.Peeker(list(file_string))
        while peeker: 
            buffer = []
            if peeker.peek().isalpha(): 
                while peeker.peek().isalnum(): 
                    buffer.append(peeker.peek())
                    peeker.next()
                peeker.back()
                buffer_string = "".join(buffer)
                if buffer_string in types: 
                    self += Token(type=TokenType.TYPE, value=buffer_string)
                else: 
                    self += Token(type=TokenType.ID, value=buffer_string)
            elif peeker.peek().isdigit():
                while peeker.peek().isdigit():
                    buffer.append(peeker.peek())
                    peeker.next()
                peeker.back()
                self += Token(type=TokenType.INT_LITERAL, value="".join(buffer))
            elif peeker.peek() in operators: 
                self += Token(type=TokenType.OPERATOR, value=peeker.peek())
            elif peeker.peek() == ";": 
                self += Token(type=TokenType.EOS)
            peeker.next()