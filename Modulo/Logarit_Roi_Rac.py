from Cryptography.Modulo.CanNguyenThuy import *
from Cryptography.Modulo.TinhModulosoLon import *
def Logarit(a,b,n):
    if(primRoots(a,n) == False):
        print('Khong co logarit roi rac')
        return
    for i in range(1,n-1):
        print(f'{i} - x = {modulo_big_num(a,i,n)}')
        if modulo_big_num(a,i,n) == b:
            return
Logarit(3,5,19)