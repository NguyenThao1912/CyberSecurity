def power(a, b, P):
    if (b == 1):
        return a
    else:
        return ((pow(a, b)) % P)


P = int(input("Enter the prime number for P:"))

G = int(input("Enter the primitve root for Q :"))

a = int(input("Enter the chosen private key A :"))

b = int(input("Enter the chosen private key B :"))

x = power(G, a, P)
y = power(G, b, P)

print('A,B=', x, y)

ka = power(y, a, P)
kb = power(x, b, P)

print("Secret key for a is :", ka)
print("Secret Key for b is :", kb)
