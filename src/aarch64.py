import prs, lex, tac

code = "int a = 1; int b = 2; int c = 3; int d = 4; int e = a * b + c * d;"
nodes = prs.run(lex.Tokens(code))
expected = [ 
    "a = 1",
    "b = 2",
    "c = 3",
    "R1_C1 = b * c",
    "d = a + R1_C1"
]

tacs = tac.run(nodes=nodes)

for t in tacs: 
    print(t)

total_vars = len(tacs) - 1
stack_size = 16 + total_vars * 16

asm = f"""\
    .globl _main
    .align 4
_main:
    stp x29, x30, [sp, -{stack_size}]!
    mov x29, sp\n\n"""


op_map = { 
    "*": "mul",
    "+": "add"
}

counter = 1
def next_offset(): 
    global counter
    offset = counter * -4
    counter += 1
    return offset

offset_map = {}
for t in tacs: 
    if t.type == tac.Type.Decl:
        offset = next_offset()
        literal = t.l
        offset_map[t.name] = offset
        asm += f"""\
    mov w8, #{literal}
    str w8, [x29, {offset}]\n\n"""
    elif t.type == tac.Type.Math: 
        offset = next_offset()
        offset_map[t.name] = offset
        asm += f"""\
    ldr w8, [x29, {offset_map[t.l]}]
    ldr w9, [x29, {offset_map[t.r]}]
    {op_map[t.op]} w8, w8, w9
    str w8, [x29, {offset}]\n\n"""

asm += F"""
    mov w0, w8
    ldp x29, x30, [sp], #{stack_size}
    ret
"""

print(asm)