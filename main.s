    .globl _main
    .align 4
_main:
    stp x29, x30, [sp, -112]!
    mov x29, sp

    mov w8, #1
    str w8, [x29, -4]

    mov w8, #2
    str w8, [x29, -8]

    mov w8, #3
    str w8, [x29, -12]

    mov w8, #4
    str w8, [x29, -16]

    ldr w8, [x29, -4]
    ldr w9, [x29, -8]
    mul w8, w8, w9
    str w8, [x29, -20]

    ldr w8, [x29, -12]
    ldr w9, [x29, -16]
    mul w8, w8, w9
    str w8, [x29, -24]

    ldr w8, [x29, -20]
    ldr w9, [x29, -24]
    add w8, w8, w9
    str w8, [x29, -28]


    mov w0, w8
    ldp x29, x30, [sp], #112
    ret