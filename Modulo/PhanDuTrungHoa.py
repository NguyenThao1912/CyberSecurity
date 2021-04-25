from TinhModulosoLon import modulo_big_num


def calculate_m(n):  # Phân tích sôs
    i = 2
    list_numbers = []
    # phân tích
    while n > 1:
        if n % i == 0:
            n = int(n / i)
            list_numbers.append(i)
        else:
            i = i + 1
    # nếu listNumbers trống thì add n vào listNumbers
    if len(list_numbers) == 0:
        list_numbers.append(n)
    return list_numbers


def calculate_a(a, k, list_num):
    a_mini = []
    for x in list_num:
        a_mini.append(modulo_big_num(a, k, x))
    return a_mini


def calculate_tall_m(n, list_m):
    M_mini = []
    for m in list_m:
        M_mini.append(n // m)
    return M_mini


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


def calculate_inverse_tall_m(list_M, list_m):
    inverse = []
    for i in range(len(list_M)):
        x = calculate_inverse(list_M[i], list_m[i])
        if x < 0:
            x = list_m[i] + x
        inverse.append(x)
    return inverse


def calculate_C(list_M, list_inverse_M):
    C = [i[0] * i[1] for i in zip(list_M, list_inverse_M)]
    return C


def calculate_X_final(list_a, list_C, M):
    s = 0
    for i in zip(list_a, list_C):
        s += i[0] * i[1]
    return modulo_big_num(s, 1, M)


def calculate_X_if_m():
    print('Nhập danh sách m :')
    list_m = [int(i) for i in input().split()]
    print('Nhập danh sach a:')
    list_a = [int(i) for i in input().split()]
    M = 1
    for x in list_m:
        M *= x
    list_M = calculate_tall_m(M, list_m)
    list_inverse_M = calculate_inverse_tall_m(list_M, list_m)
    list_C = calculate_C(list_M, list_inverse_M)
    x = calculate_X_final(list_a, list_C, M)
    print('Danh sách m nhỏ là : ', list_m)
    print('Danh sách a là : ', list_a)
    print('Danh sách M là : ', list_M)
    print('Danh sách nghịch đảo M là : ', list_inverse_M)
    print('Danh sách C là : ', list_C)
    print('x = ', x)


def calculate_X_for_akn():
    a = int(input('Nhập a = '))
    k = int(input('Nhập k = '))
    n = int(input('Nhập n = '))
    list_m = calculate_m(n)
    list_a = calculate_a(a, k, list_m)
    list_M = calculate_tall_m(n, list_m)
    list_inverse_M = calculate_inverse_tall_m(list_M, list_m)
    list_C = calculate_C(list_M, list_inverse_M)
    x = calculate_X_final(list_a, list_C, n)
    print('Danh sách m nhỏ là : ', list_m)
    print('Danh sách a là : ', list_a)
    print('Danh sách M là : ', list_M)
    print('Danh sách nghịch đảo M là : ', list_inverse_M)
    print('Danh sách C là : ', list_C)
    print('x = ', x)

if __name__ == '__main__':
    #Tính toán cho a,k,n
    #calculate_X_for_akn()
    #Tính toán cho danh sách m,a
    calculate_X_if_m()
