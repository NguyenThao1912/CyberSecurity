import random
from math import sqrt


def calculated(x: int, y: int, p: int):
    '''
    (x^y) % p
    :param x:giá trị x
    :param y:giá trị y (với y >=0)
    :param p:giá trị p
    :return: trả về (x^y) %p
    '''
    result = 1
    x = x % p
    while y > 0:
        # kt nếu y lẻ
        if y % 2 == 1:
            # thì ta lấy kết quả * x
            result = (result * x) % p
        # y bây giờ chắc chắn sẽ lẻ
        y = y // 2
        x = (x * x) % p
    return result


def millertest(d: int, n: int):
    '''
    :param d: giá trị d
    :param n: giá trị n
    :return: True / False
    '''
    a = 2 + random.randint(2, n - 2) % (n - 4)

    # tính toán a ^d % n
    x = calculated(a, d, n)

    if x == 1 or x == n - 1:
        return True
    # tiếp tục bình phương x đến khi 1 trong những điều này xảy ra
    # (1) d  chưa tới n-1
    # (2) (x^2) % n không phải 1
    # (3) (x^2) %n không phải n-1
    while d != n - 1:  # (1)
        x = (x * x) % n
        d = d * 2
        if x == 1:
            return False  # (2)
        if x == n - 1:
            return True  # (3)
    return False


def isprime_miller(n: int, k: int):
    '''
        Hàm Kiểm tra nguyên tố
        :param n: GIÁ TRỊ N
        :param k: GIÁ TRỊ k (k càng lớn độ chính xác càng cao)
        :return: TRUE/FAlSE
    '''
    # Base case
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d = d // 2
    for _ in range(k):
        if not millertest(d, n):
            return False
    return True


def prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print(prime(4346))
