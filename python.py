import hashlib
text = input("Enter text here : ")
h = hashlib.md5(text.encode())
md_hash = h.hexdigest()
print(md_hash)
