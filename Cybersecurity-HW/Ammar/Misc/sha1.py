from bitarray import bitarray
from bitarray.util import hex2ba
from bitarray.util import ba2hex

class SHA1:
    def __init__(self):
        self.message = ''
        self.ba = bitarray()
        self.block_size = 512
        self.a = hex2ba("67452301")
        self.b = hex2ba("efcdab89")
        self.c = hex2ba("98badcfe")
        self.d = hex2ba("10325476")
        self.e = hex2ba("c3d2e1f0")
        self.k = [hex2ba("5a827999"), hex2ba("6ed9eba1"), hex2ba("8f1bbcdc"), hex2ba("ca62c1d6")]



    def digest(self, m):
        self.message = m
        self.ba.frombytes(m.encode('ascii'))
        length = len(self.ba)
        self.ba.append(1)
        self.ba.extend([0]*(447-length))
        length_ba = bitarray(format(length,"b").zfill(64))
        self.ba.extend(length_ba)


    
    def f1(self): return hex((self.b or self.c) and (self.b or self.d))
    #def f1(self): return hex((self.b or self.c) and (self.b or self.d))
    #def f1(self): return hex((self.b or self.c) and (self.b or self.d))
    #def f1(self): return hex((self.b or self.c) and (self.b or self.d))

    #def f(self, stage):
    #    match stage:
    #        case 1:
    #        case 2:
    #            print()
    #        case 3:
    #            print()
    #        case 4:
    #            print()
    #        case _:
    #            print()