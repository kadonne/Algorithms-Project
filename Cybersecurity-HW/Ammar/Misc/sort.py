def main():
   f = open('encrypted_passwords.txt','r')
   r = sorted(f.readlines())
   for i in r:
    print(i.strip())
main()