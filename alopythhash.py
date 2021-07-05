import hashlib
text = "Some of us are good.".encode()
print("SHA-256: ", hashlib.sha256(text).hexdigest())
print("SHA-3-256",hashlib.sha3_256(text).hexdigest())
print("BLAKE2c",hashlib.blake2s(text).hexdigest())