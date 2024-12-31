import lex, prs

code = "int a = 1; int b = 2; int c = 3; int d = a + b * c;"
tokens = lex.Tokens(code)
nodes = prs.run(tokens)

expected = [ 
    prs.Decl(name="a", value=prs.Lit(value="1")),
    prs.Decl(name="b", value=prs.Lit(value="2")),
    prs.Decl(name="c", value=prs.Lit(value="3")),
    prs.Decl(
        name="d", 
        value=prs.Bin(
            l=prs.Ref(value="a"),
            r=prs.Bin(
                l=prs.Ref(value="b"),
                r=prs.Ref(value="c"),
                op="*"
            ), 
        op="+")
    )
]

assert nodes.__repr__() == expected.__repr__() # high quality test