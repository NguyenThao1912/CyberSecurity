import string

def ciphertext(text,d):
    result = ''
    for i in range(len(text)):
        if text[i] == ' ':
            result += ' '
            continue
        result += d[text[i]]
    return result

def originaltext(ciphertext,d):
    result = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            result += ' '
            continue
        result += d[ciphertext[i]]
    return result

if __name__ == '__main__':
    #bang chu cai
    alphabet = list(string.ascii_lowercase)
    # nhap du lieu
    plaintext = input().lower()
    keys = list(input().lower())
    # tu dien
    d = {}
    d2 ={}
    #danh dau vi tri vd a - >  h , b-> f
    for i in range(len(alphabet)):
        d[alphabet[i]] = keys[i]
    #danh dau vi tri de giai ma vd h -> a , f ->b
    for i in range(len(alphabet)):
        d2[keys[i]] = alphabet[i]
    #ma hoa
    cipher = ciphertext(plaintext,d)
    #giai ma
    origin = originaltext(cipher,d2)
    print(cipher.upper())
    print(origin.upper())
