	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 1
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
; %bb.0:
	sub	sp, sp, #16
	str	wzr, [sp, #12]
	mov	w8, #7                          ; =0x7
	str	w8, [sp, #8]
	ldr	w0, [sp, #8]
	add	sp, sp, #16
	ret
                                        ; -- End function
.subsections_via_symbols
