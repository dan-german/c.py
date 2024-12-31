import lex 
from enum import Enum
from utils import *

prec = { "+": 1, "-": 1, "*": 2, "/": 2 }

class Type(Enum): 
    Decl = 1
    Assign = 2
    Math = 3
    Lit = 4
    Ref = 5
    Bin = 6

class ASTExpr:
    def __repr__(self, indent = ""): return f"{indent}{self.type.name}"
    def __init__(self, *, type: Type, value): 
        self.type = type
        self.value = value

class Decl(ASTExpr): 
    def __repr__(self, indent = ""): 
        base = indent + super().__repr__() # value: 
        base += nl + indent + f"{self.name}" # id: 
        base += nl + indent + self.value.__repr__(space*4)
        return base
    def __init__(self, *, name: str, value: ASTExpr = None):
        super().__init__(type=Type.Decl, value=value)
        self.name = name

class Bin(ASTExpr): 
    def __repr__(self, indent = ""):
        base = super().__repr__(indent) + f" {self.op}"
        if self.l: base += nl + indent + "  L: " + nl + self.l.__repr__(indent + space*4)
        if self.r: base += nl + indent + "  R: " + nl + self.r.__repr__(indent + space*4)
        return base
    def __init__(self,*, l: ASTExpr, r: ASTExpr, op: str): 
        super().__init__(type=Type.Bin, value="")
        self.op = op
        self.l = l
        self.r = r
    def bin_leaf(self): return self.l.type != Type.Bin and self.r.type != Type.Bin
    def semi_bin_leaf(self): return self.l.type == Type.Bin or self.r.type == Type.Bin

class Lit(ASTExpr): 
    def __repr__(self, indent = ""): return super().__repr__(indent) + f" ({self.value})"
    def __init__(self,*,value: str): super().__init__(type=Type.Lit, value=value)

class Ref(ASTExpr):
    def __repr__(self, indent=""): return super().__repr__(indent) + f" ({self.value})"
    def __init__(self, *, value: str): super().__init__(type=Type.Ref, value=value)

def climb(l, min_prec, peeker): # todo: figure out the iterative solution
    while peeker and peeker.peek().type != lex.TokenType.EOS and prec[peeker.peek().value] > min_prec:
        op = peeker.next()
        r = token_value_to_ast(peeker.next())
        if peeker and peeker.peek().type != lex.TokenType.EOS and prec[peeker.peek().value] > prec[op.value]:
            r = climb(r, prec[op.value], peeker)
        l = Bin(l=l, r=r, op=op.value)
    return l

def token_value_to_ast(tok):
    return Lit(value=tok.value) if tok.type == lex.TokenType.INT_LITERAL else Ref(value=tok.value)

def parse_type(peeker):
    id = peeker.peek(1)
    peeker.next(3)
    if peeker.peek(1).type == lex.TokenType.EOS: 
        return Decl(name=id.value, value=Lit(value=peeker.peek().value))
    return Decl(name=id.value, value=climb(token_value_to_ast(peeker.next()), 0, peeker))

def run(tokens: lex.Tokens):
    peeker = Peeker(tokens.tokens)
    nodes = []
    while peeker: 
        nxt = peeker.peek()
        if nxt.type == lex.TokenType.TYPE:
            nodes.append(parse_type(peeker))
        peeker.next()
    return nodes