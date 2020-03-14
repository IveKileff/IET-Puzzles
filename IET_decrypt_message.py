'''this program aims to decrypt the message given.
notes:
    that A = 65, B = 66 etc
    and that  a = 97, b = 98 etc
    ord(A) returns ascii value for letter
    chr(65) returns letter for ascii value
    int() tells python that the item is a number
    ^ is an xor function
'''


message = [1,9,9,24,1,9,3,25,24,31,5,8,9,24,4,9,15,13,10,9,5,2,4,
           13,0,10,13,2,4,3,25,30,13,2,8,8,3,2,24,24,9,0,0,15,4,13,30,0,9,31]
orig_msg = []
possible_keys = []

'''generate a list of possible keys'''
for number in range(65,91):
    possible_keys.append(chr(number))

'''create a list with the numbers in the message converted into ASCII'''
for number in message:
    orig_msg.append(chr(number))

'''put the message through all the poss keys and print it'''
for key in possible_keys:
    de_encrypted_msg = []
    k = int(ord(key))
    for no in message:
        de_encrypted_msg.append(chr(no ^ k))
    de_encrypted_option = "".join(de_encrypted_msg)
    if 'THE' in de_encrypted_option:
        print(f'The key may be: {key}, in which case the message is:')
        print(f'{de_encrypted_option}\n')
else:
    reply = input('Do you want to see all the options (Y/N)?')
    if reply is 'Y':
        for key in possible_keys:
            de_encrypted_msg = []
            k = int(ord(key))
            for no in message:
                de_encrypted_msg.append(chr(no ^ k))
            de_encrypted_option = "".join(de_encrypted_msg)
            print(f'For key {key}:\n{de_encrypted_option}')
    if reply is 'N':
        print('Cheerio')

    

    

