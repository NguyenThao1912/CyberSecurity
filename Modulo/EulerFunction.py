def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi(n):
    result = 1
    #duyệt từ 2 -> n-1 đếm xem có bn số gcd(i,n) == 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result
if __name__ == '__main__':
    x = int(input("Nhap n"))
    print("Gia tri Ham Euler la : ",phi(x))