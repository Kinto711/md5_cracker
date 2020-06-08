import hashlib

flag =0
pass_hash = input("Enter the md5 hash: ")

original_file = '1MillionPassword.txt'


try:
    opened_file = open (original_file, 'r')
except:
    print("File not Found")
    quit
for pswd in opened_file:
    enc_wrd = pswd.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("The password is " + pswd)
        flag = 1
        break
if flag == 0:
    print("Password not found.")
