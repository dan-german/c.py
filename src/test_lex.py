import lex

def test():
    expected = lex.Tokens("")
    expected += lex.Token(type=lex.TokenType.TYPE, value="int")
    expected += lex.Token(type=lex.TokenType.ID, value="a")
    expected += lex.Token(type=lex.TokenType.OPERATOR, value="=")
    expected += lex.Token(type=lex.TokenType.INT_LITERAL, value="1")
    expected += lex.Token(type=lex.TokenType.EOS)

    expected += lex.Token(type=lex.TokenType.TYPE, value="int")
    expected += lex.Token(type=lex.TokenType.ID, value="b")
    expected += lex.Token(type=lex.TokenType.OPERATOR, value="=")
    expected += lex.Token(type=lex.TokenType.ID, value="a")
    expected += lex.Token(type=lex.TokenType.EOS)

    assert expected == lex.Tokens("int a = 1; int b = a;")
    print("lex good 👍")

test()