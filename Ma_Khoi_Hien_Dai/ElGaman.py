import random
from Cryptography.Modulo.TinhModulosoLon import *
def calculate_inverse(num, modulo):
    ri_1, ri_2 = modulo, num
    xi_1, yi_1 = 1, 0
    xi_2, yi_2 = 0, 1
    ri_new, qi_new, xi_new, yi_new = 0, 0, 0, 0
    i = 1
    while True:
        ri_new = ri_1 % ri_2
        qi_new = ri_1 // ri_2
        xi_new = xi_1 - (qi_new * xi_2)
        yi_new = yi_1 - (qi_new * yi_2)
        if ri_new == 0:
            break
        i += 1
        ri_1, xi_1, yi_1 = ri_2, xi_2, yi_2
        ri_2, xi_2, yi_2 = ri_new, xi_new, yi_new

    return yi_2
def calculate_y_a(a,x_a,q):
    return modulo_big_num(a,x_a,q)
def calculate_c1_c2(a,q,k,M,y_a):

    '''
    :param a: căn nguyên thủy của q
    :param q: số nguyên tố đề bài cho
    :param k: khóa đề cho
    :param M: Bản mã
    :param y_a: Khóa công khai
    :return: Bản Mã (C1 - C2)
    '''
    # K = (YA)^k mod q

    K = modulo_big_num(y_a,k,q)

    # C1 = a^k mod q
    C1 = modulo_big_num(a,k,q)

    # C2 = K*M^1 mod q
    C2 = modulo_big_num(K*M,1,q)

    return (C1,C2)
def decrypt(C1,C2,X_a,q):
    '''
    :param C1: Bản mã C1
    :param C2: Bản mã C2
    :param X_a: khóa công khai của A
    :param q: số nguyên tố đề cho
    :return: Bản rõ M =
    '''
    # K = (C1)^Xa mod q
    K = modulo_big_num(C1,X_a,q)

    # K ^ -1
    inverse_K = calculate_inverse(K,q)

    #M = (C2*K^-1) mod q

    M = modulo_big_num(C2*inverse_K,1,q)
    return M

if __name__ == '__main__':
    q = 6827
    a = 5
    xA = 307
    k = 919
    M = 474
    #===== khai báo bla bla
    yA,C1,C2 = 1,1,1

    #Tinh  Ya

    yA = calculate_y_a(a,xA,q)
    # Tinh C1 C2

    C1,C2 = calculate_c1_c2(a,q,k,M,yA)

    # DIch nguoc ban ma
    M = decrypt(C1,C2,xA,q)

    print(f'PU = ({q},{a},{xA}) ')
    print(f'(C1,C2) = ({C1}, {C2})')
    print(f'M = {M}')