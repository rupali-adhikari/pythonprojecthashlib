import hashlib
a = hashlib.pbkdf2_hmac("sha256", b"hallo", b"salt", 1)
b = hashlib.pbkdf2_hmac("sha256", a, b"salt", 1)
c = hashlib.pbkdf2_hmac("sha256", b"hallo", b"salt", 2)
print(b)
print(c)