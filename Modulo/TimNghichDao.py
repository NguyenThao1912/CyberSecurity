# Expand Euclid

def NghichDao(num, modulo):
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
        data = [ri_new, qi_new, xi_new, yi_new]
        print(str(i) + " {: >10} {: >10} {: >10} {: >10}".format(*data))
        i += 1
        ri_1, xi_1, yi_1 = ri_2, xi_2, yi_2
        ri_2, xi_2, yi_2 = ri_new, xi_new, yi_new
    print()
    print(f"Inverse of {num} ^(-1) mod {modulo} la : {yi_2}")
    print()
    print(f"Inverse of {modulo} ^(-1) mod {num} la : {xi_2}")


if __name__ == '__main__':
    print('Calculate inverse modulo of a^(-1) mod b ')
    a = int(input('Value Of  a : '))
    b = int(input('Value Of  b : '))
    print()
    NghichDao(a,b)
