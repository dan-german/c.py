import tac, lex, prs
from collections import defaultdict

def test():
    code = "int a = 1; int b = 2; int c = 3; int d = a + b * c;"
    nodes = prs.run(lex.Tokens(code))
    expected = [ 
        tac.Tac(tac.Type.Decl, "a", 1),
        tac.Tac(tac.Type.Decl, "b", 2),
        tac.Tac(tac.Type.Decl, "c", 3),
        tac.Tac(tac.Type.Math, "R1_C1", "b", "*", "c"),
        tac.Tac(tac.Type.Math, "d", "a", "+", "R1_C1")
    ]

    print(tac.run(nodes=nodes))
    print(expected)

    assert expected.__repr__() == tac.run(nodes=nodes).__repr__()

def test2():
    code = "int a = 1; int b = 2; int c = 3; int d = 4; int e = a * b + c * d;"
    nodes = prs.run(lex.Tokens(code))

    expected = [ 
        tac.Tac(tac.Type.Decl, "a", 1),
        tac.Tac(tac.Type.Decl, "b", 2),
        tac.Tac(tac.Type.Decl, "c", 3),
        tac.Tac(tac.Type.Decl, "d", 4),
        tac.Tac(tac.Type.Math, "R1_C1", "b", "*", "c"),
        tac.Tac(tac.Type.Math, "d", "a", "+", "R1_C1")
    ]
    print(tac.run(nodes=nodes))
    assert expected == tac.run(nodes=nodes)

test()
test2()