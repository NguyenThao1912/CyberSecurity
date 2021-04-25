def sqr(n):
    return n * n


def pow(a, b):
    if b == 0:
        return 1
    else:
        if b % 2 == 0:
            return sqr(pow(a, b // 2))
        else:
            return a * (sqr(pow(a, b // 2)))

def modulo_big_num(a,b,c):
    return pow(a,b) % c

if __name__ == '__main__':
    a ,b,c = map(int,input().split())
    print(modulo_big_num(a,b,c))