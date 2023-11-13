import hashlib
import random
import math
import sys
def main():
    sample_size = 0
    size_factor = 0
    hash_function = 0
    try:
        sample_size = int(sys.argv[1]) 
        size_factor = int(sys.argv[2])
        hash_function = int(sys.argv[3])
    except Exception:
        print('Usage: python make_data.py <sample_size>, <size_factor>, <hash_function>\nExpected int in command-line arguements.')
        quit()

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>']
    digits = ['0','1','2','3','4','5','6','7','8','9']

    lowercased = open('words-original.txt','r')
    write_file = open('words.txt','w')
    password_file = open('encrypted_passwords.txt','w')
    words = lowercased.read().splitlines()
    line_numbers = list()
    for i in range(0,size_factor):
        line_numbers.append(random.randint(0,len(words)-1))
    for number in line_numbers:
        length = number+math.floor(sample_size/size_factor)
        if length>len(words): length = len(words)
        for i in range(number,length):
            write_file.write(words[i]+'\n')

    for i in line_numbers:
        length = i+math.floor(sample_size/size_factor)
        if length>len(words): length = len(words)
        clear_text_sd = words[random.randint(i,length)] + symbols[random.randint(0,len(symbols)-1)] + digits[random.randint(0,len(digits)-1)]
        clear_text_ds = words[random.randint(i,length)] + digits[random.randint(0,len(digits)-1)] + symbols[random.randint(0,len(symbols)-1)] 
        password_file.write(encrypt_string(clear_text_sd,hash_function)+'\n'+encrypt_string(clear_text_ds,hash_function)+'\n')
        #print(clear_text_sd)
        #print(clear_text_ds)

    lowercased.close()
    write_file.close()
    password_file.close()

def encrypt_string(password, hash_function):
    if hash_function == 32:
        return str(hashlib.md5(password.encode()).hexdigest())
    elif hash_function == 40:
        return str(hashlib.sha1(password.encode()).hexdigest())
    elif hash_function == 56:
        return str(hashlib.sha224(password.encode()).hexdigest())
    elif hash_function == 64:
        return str(hashlib.sha256(password.encode()).hexdigest())
    elif hash_function == 96:
        return str(hashlib.sha384(password.encode()).hexdigest())
    return ''

main()