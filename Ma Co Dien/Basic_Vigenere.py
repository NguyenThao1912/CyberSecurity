import string
alphabet = list(string.ascii_lowercase)
print(alphabet)
d ={}
temp = 0
for i in alphabet:
    d[i] = temp
    temp +=1
plaintext = input("Please input your plain text :")
keys = input("please input your key:")
if any(i.isdigit() for i in keys):
    print("key cannot contain number ")

keys = keys.lower()
plaintext = list(plaintext.lower())

def VigenereEncode(plaintext,keys):
    global d
    encodekey = []
    if len(keys) > len(plaintext):
        for i in range(len(plaintext)):
            encodekey.append(keys[i])
    else:
        encodekey = list(keys[::])
        l = len(keys)
        x = 0
        for i in range(l, len(plaintext)):
            if x >= l:
                x = 0
            encodekey.append(keys[x])
            x += 1

    for i in range(len(plaintext)):
        encodekey[i] = d[encodekey[i]]
        plaintext[i] = d[plaintext[i]]
    result = []
    for i, j in zip(encodekey, plaintext):
        result.append(alphabet[(i + j) % 26])
    return "".join(result)

def VigenereDecode(Code,keys):
    global d
    encodekey = []
    if len(keys) > len(Code):
        for i in range(len(Code)):
            encodekey.append(keys[i])
    else:
        encodekey = list(keys[::])
        l = len(keys)
        x = 0
        for i in range(l, len(Code)):
            if x >= l:
                x = 0
            encodekey.append(keys[x])
            x += 1
        for i in range(len(Code)):
            encodekey[i] = d[encodekey[i]]
            Code[i] = d[Code[i]]
        result = []
        for i, j in zip(Code, encodekey):
            result.append(alphabet[(i - j) % 26])
        return "".join(result)
en = VigenereEncode(plaintext,keys)
print('Cipher text',en.upper())
de = VigenereDecode(list(en),keys)
print('text after decode ',de.upper())