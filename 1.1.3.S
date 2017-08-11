.global your_asm_fn

.section .data

mp: .long 0xc001f00d

.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
lea mp,%eax
pushl %eax
pushl $0xc105ed
pushl $0xacce55ed
call practice

leave
ret

