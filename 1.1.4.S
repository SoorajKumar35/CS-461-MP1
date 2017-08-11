.global your_asm_fn

.section .data

str: 
	.string "coolfood"

sec:
	.long 0xc105ed

.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

leal str, %eax
pushl %eax
leal sec,%eax
pushl %eax
pushl $0xacce55ed
call practice
leave
ret