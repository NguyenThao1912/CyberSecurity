class Playfair():
    '''
    Sets up a playfair cipher based on key supplied, used to encrypt and 
    decrypt.
    '''

    def __init__(self, text):
        '''Builds cipher so that it can be used to encrypt and decrypt text.'''

        self.text = text
        '''Bảng chữ cái'''
        self.alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', \
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
                      'x', 'y', 'z']

        combo = list(self.text)
        ''' key + bảng chữ cái '''
        combo += self.alpha
        '''cipher chứa bảng khóa '''
        cipher = []

        for char in combo:
            '''nếu kí tự CHƯA được thêm vào cipher và kí tự ở trong bảng chữa cái '''
            if char not in cipher and char in self.alpha:
                cipher.append(char)
            else:
                pass
        '''Sinh ma trận 5-5 '''
        cipher = [cipher[:5], cipher[5:10], cipher[10:15], cipher[15:20], \
                  cipher[20:25]]

        self.cipher = cipher

    def __str__(self):
        '''Returns the cipher in grid form.'''

        cipher = '\n'

        for line in self.cipher:
            for char in line:
                cipher += (char + ' ')
            cipher += '\n'

        return cipher[:-1] + '\n'

    def row(self, char):
        '''Finds the row for a character in the cipher grid.'''

        position = 0
        counter = 0
        for line in self.cipher:
            if char in line:
                position = counter
            counter += 1

        return position

    def col(self, char):
        '''Finds the column for a character in the cipher grid.'''

        position = 0
        for line in self.cipher:
            counter = 0
            for letter in line:
                if char == letter:
                    position = counter
                counter += 1

        return position


def encrypt(key, message):
    '''Encrypts a message Using a playfair cipher using a given key'''
    #Sinh khóa
    cipher = Playfair(key)

    prev_char = message[0]
    mess = prev_char
    # nếu kí tự đầu là j thì thay thế = i
    mess.replace('j', 'i')

    for char in message[1:]:
        # nếu 2 chữ giống nhau đứng cạnh nhau vd aa thì thêm q vào giữa
        if char == prev_char:
            mess += ('q')
        # nếu kí tự trong bảng chữ cái thì thêm bt và cập nhật chữ cái gần nhất
        if char in cipher.alpha:
            mess += (char)
            prev_char = char

    # nếu độ dài tin nhắn k phải là 1 số chẵn (do phải tách thành các cặp )
    if len(mess) % 2 != 0:
        mess += 'q'
    # tách mảng message ra thành các cặp vd axbycz => ax by cz
    mess = [mess[i:i + 2] for i in range(0, len(mess), 2)]

    ciphertext = ''
    # bắt đầu sinh mã với mỗi cặp sinh được ở trên
    for pair in mess:
        final_pair = ''
        '''nếu 2 chữ cùng hàng =)'''
        if cipher.row(pair[0]) == cipher.row(pair[1]):
            for i in pair:
                if cipher.col(i) == 4:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][0]

                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][cipher.col(i) + 1]

            ciphertext += final_pair + ' '
        #nếu 2 chữ cùng cột
        elif cipher.col(pair[0]) == cipher.col(pair[1]):
            for i in pair:
                if cipher.row(i) == 4:
                    final_pair += cipher.cipher[0][cipher.col(i)]

                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row + 1][cipher.col(i)]

            ciphertext += final_pair + ' '
        #còn không thì lấy hàng của chữ này và cột chữ kia
        else:
            first = [cipher.row(pair[0]), cipher.col(pair[0])]
            second = [cipher.row(pair[1]), cipher.col(pair[1])]

            final_pair = cipher.cipher[first[0]][second[1]] \
                         + cipher.cipher[second[0]][first[1]]

            ciphertext += final_pair + ' '
    #lấy mảng kq đến -1 thôi vì bỏ dâu cách ở trên ' ' =)
    return ciphertext[:-1]


def decrypt(key, text):
    ''' Decrypts a message Using a playfair cipher using a given key '''

    cipher = Playfair(key)
    plaintext = ''

    if type(text) == str:
        text = text.split(' ')
    #decrypt làm ngược lại thui =))
    for pair in text:
        final_pair = ''
        #cùng hàng
        if cipher.row(pair[0]) == cipher.row(pair[1]):

            for i in pair:
                if cipher.col(i) == 0:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][4]

                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][cipher.col(i) - 1]

            plaintext += final_pair
        #cùng cột
        elif cipher.col(pair[0]) == cipher.col(pair[1]):
            for i in pair:
                if cipher.row(i) == 0:
                    final_pair += cipher.cipher[4][cipher.col(i)]

                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row - 1][cipher.col(i)]

            plaintext += final_pair
        #khác hàng khác cột
        else:
            first = [cipher.row(pair[0]), cipher.col(pair[0])]
            second = [cipher.row(pair[1]), cipher.col(pair[1])]

            final_pair = cipher.cipher[first[0]][second[1]] \
                         + cipher.cipher[second[0]][first[1]]

            plaintext += final_pair

        if plaintext[-1] == 'q':
            plaintext = plaintext[:-1]

        counter = 0
        final = ''

        for i in plaintext:
            if i == 'q' and plaintext[counter - 1] == plaintext[counter + 1]:
                pass
            else:
                final += i
            counter += 1

    return final


if __name__ == '__main__':
    print('Type in your key and message ')
    message = input('Your message : ')
    key = input('Your key : ')
    new_cipher = Playfair(key.lower())

    print(new_cipher)
    cipher = encrypt(key.lower(), message.lower())
    decrypt = decrypt(key.lower(), cipher)
    print('encrypt : ', cipher)
    print('decrypt : ', decrypt)
