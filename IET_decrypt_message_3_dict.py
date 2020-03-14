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
poss_solutions_dict = {}

def decrypt_msg(k):
    '''put the message through the passed key and return a string with the possible solution'''
    for item in message:
        de_encrypted_msg.append(chr(item ^ k))
    possible_solution = "".join(de_encrypted_msg)
    return possible_solution

'''create a list with the numbers in the message converted into ASCII'''
for number in message:
    orig_msg.append(chr(number))
    
'''generate a list of possible keys'''
for number in range(65,91):
    possible_keys.append(chr(number))

'''passes message through possible keys and add them to a dictionary'''
for key in possible_keys:
    de_encrypted_msg = []
    k = int(ord(key))
    poss_solution = decrypt_msg(k)
    poss_solutions_dict[chr(k)] = poss_solution
    if 'THE' in poss_solution:
        print(f'The key may be: {key}, in which case the message is:')
        print(poss_solution)
        print('\n')

reply = input('Do you want to see all the options (Y/N)?')
if reply is 'Y':
    for key, value in poss_solutions_dict.items():
        print(f'For key {key} the message would be {value}')
if reply is 'N':
    print('Cheerio')
if reply not in ('N', 'Y'):
    print("I don't know what to do so I'm stopping work!")













        






