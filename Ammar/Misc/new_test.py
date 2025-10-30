from bitarray import bitarray
from bitarray.util import hex2ba
from bitarray.util import ba2hex
def main():
    b = "67452301"
    h = hex2ba(b)
    print(bin(0x67452301))
    a = hex2ba("67452301")
    b = hex2ba("efcdab89")
    c = hex2ba("98badcfe")
    d = hex2ba("10325476")
    e = hex2ba("c3d2e1f0")
    k = [hex2ba("5a827999"), hex2ba("6ed9eba1"), hex2ba("8f1bbcdc"), hex2ba("ca62c1d6")]
    print(h)
    print(len(h))
    m = 'Supercalifragilisticexpialidocious'
    ba = bitarray()
    ba.frombytes(m.encode('ascii'))
    length = len(ba)
    ba.append(1)
    ba.extend([0]*(447-length))
    length_array = bitarray(format(length,"b").zfill(64))
    ba.extend(length_array)
    print(ba)
    chunks = []
    for i in range(0,len(ba),32):
        chunks.append(ba[i:i+32])
    print(W_function_80_rounds(ba))

def W_function_80_rounds(chunks):
    a16 = 0
    b16 = 0
    c16 = 0
    d16 = 0
    for i in range(16,81):
        a16 = chunks[i-3:i+32-3]
        b16 = chunks[i-8:i+32-8]
        c16 = chunks[i-14:i+32-14] 
        d16 = chunks[i-16:i+32-16] 
    print(a16,b16,c16,d16)
    xorA = a16 ^ b16
    xorB = xorA ^ c16
    xorC = xorB ^ d16
    xorC <<= 1
    return xorC
    
        
    #print(ba)
    #print(len(ba))

main()