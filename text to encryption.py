#_*_ coding: utf-8 _*_
import hashlib

print("What encryption would you like to use?")
print("0. sha1")
print("1. sha224")
print("2. sha256")
print("3. sha384")
print("4. sha512")
print("5. md5")
print("")
encType = input('Input your selection')
print(" ")
if encType == "0":
    print('Input text to encrypt')
    a = input()
    result = hashlib.sha1(a.encode())
    print("Your SHA1 encrypted text is: ")
    print(result.hexdigest())

elif encType == '1':
    print('Input text to encrypt')
    i = input()
    result = hashlib.sha224(i.encode())
    print("Your SHA224 encrypted text is: ")
    print(result.hexdigest())

elif encType == '2':
    print('Input text to encrypt')
    c = input()
    result = hashlib.sha256(c.encode())
    print("Your SHA256 encrypted text is: ")
    print(result.hexdigest())

elif encType == '3':
    print('Input text to encrypt')
    b = input()
    result = hashlib.sha384(b.encode())
    print("Your SHA384 encrypted text is: ")
    print(result.hexdigest())

elif encType == '4':
    print('Input text to encrypt')
    d = input()
    result = hashlib.sha512(d.encode())
    print("Your SHA512 encrypted text is: ")
    print(result.hexdigest())

elif encType == '5':
    print('Input text to encrypt')
    e = input()
    result = hashlib.md5(e.encode())
    print("Your MD5 encrypted text is: ")
    print(result.hexdigest())
