import string
def ceasar(arr, keys, type):
    alphabet = list(string.ascii_lowercase)
    encode = []
    if type == 1:  # 1 is encoding
        for i in arr:
            for j in range(len(i)):
                    encode.append(alphabet[(alphabet.index(i[j]) + keys) % 26])
    else:          #else is decode
        for i in arr:
            for j in range(len(i)):
                encode.append(alphabet[(alphabet.index(i[j]) - keys) % 26])
    return "".join(encode)
if __name__ == '__main__':
    plain_text = input('Nhập plain text : ')
    key = int(input('Nhập số kí tự dịch : '))
    encode = ceasar(plain_text.lower(),key,1)
    print('Encode : ',encode)
    print('=======================')
    decode = ceasar(encode,key,2)
    print('Decode : ',decode)