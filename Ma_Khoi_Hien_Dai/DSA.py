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
def calculate_y_a(g,p,x_a):
    '''

    :param g: giá trị g
    :param p: giá trị p
    :param x_a: giá trị x
    :return: giá trị y_a
    '''
    return modulo_big_num(g,x_a,p)

#Sinh chữ kí số
def calculate_signature(k, h_m, g,p,q,x_a):
    r = modulo_big_num(modulo_big_num(g,k,p),1,q)

    inverse_k = calculate_inverse(k,q)
    s = modulo_big_num(inverse_k * (h_m + x_a * r),1,q)
    return (r,s)

#Kiểm tra chữ ký
def check_signature(s,r,h_m,p,q,g,y):
    # s^-1 mod q
    inverse_s = calculate_inverse(s,q)
    # w = s^-1 mod q
    w = inverse_s
    # u1 = (H(M)*w) mod q
    u1 = modulo_big_num(h_m*w,1,q)
    # u2 = (r*w) mod q
    u2 = modulo_big_num(r*w,1,q)

    # gy =  g^u1 mod p * g^u2 mod q
    gy = modulo_big_num(g,u1,p) * modulo_big_num(y,u2,p)
    # gy = gy mod p
    gy = modulo_big_num(gy,1,p)

    # v = gy mod q
    v = modulo_big_num(gy,1,q)

    if v == r:
        return 'Chu Ky Dung'
    return 'Chu Ky Sai'

if __name__ == '__main__':
    p = 23
    q = 11
    h = 7
    x_a= 5
    k = 6
    h_m = 9
    #=======
    g = modulo_big_num(h, 2, p)
    #=========
    y_a = calculate_y_a(g,p,x_a)

    r,s = calculate_signature(k,h_m,g,p,q,x_a)
    print('y_a = ' ,y_a )
    print(f'(r,s) = ({r},{s})' )
    print(check_signature(s,r,h_m,p,q,g,y_a))

