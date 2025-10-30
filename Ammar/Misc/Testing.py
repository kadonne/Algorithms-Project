a = 0x67452301
b = 0xefcdab89
c = 0x98badcfe
d = 0x10325476
e = 0xc3d2e1f0

k = 0b1011110110011001
f = 0b1100001110000101

def f1():  
    res = hex(a^b)
    print(hex(a))
    print(hex(b))
    print(hex(a^b))
    return res

print(f1())