from Cryptography.Modulo.EulerFunction import phi
from PhanDuTrungHoa import calculate_m as PhantichSo
from TinhModulosoLon import modulo_big_num
def primRoots(a,modulo):
    t = phi(modulo)
    # check co-prime number with modulo
    nguyento = PhantichSo(t)
    for x in nguyento:
        if modulo_big_num(a,t//x,modulo) == 1:
            return False
    return True
if __name__ == '__main__':
    x = int(input('Nhập số n : '))
    modulo = int(input('Nhập Số modulo : '))
    if primRoots(x,modulo):
        print(f'{x} là căn nguyên thủy của {modulo}')
    else:
        print(f'{x} không là căn nguyên thủy của {modulo}')