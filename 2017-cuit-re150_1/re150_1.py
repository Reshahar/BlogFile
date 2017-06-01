list = [0x73,0x8d,0xf2,0x4c ,0xc7 ,0xd4 ,0x7b ,0xf7 ,0x18 ,0x32 ,0x71 ,0x0d ,0xcf ,0xdc ,0x67 ,0x4f,0x7f,0x0b ,0x6d]
ret=[]

for i in list:
    ret.append(hex(i^32))
print ret
k = 0
x = 0
flag = ''
for i in ret:
    for j in range(0,256):
        x = k & 7
        z = ((j>>x)|(j<<(8-x)))
        y = z^k
        y = y%256
        #print y
        if y==int(i,16):
            flag+=chr(j)
    k = k+1
print flag
