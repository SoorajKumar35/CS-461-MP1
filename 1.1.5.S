.global _main

.section .data

shell:
	.asciz "/bin/sh"


.section .text

_main:

push	%ebp
mov	%esp,%ebp

subl $8,%esp
movl $shell,%edi
movl 12(%ebp),%ecx

movl $shell,%ebx
movl 12(%ebp),%ecx
movl 16(%ebp),%edx
movl $11, %eax

int $0x80

leave
ret