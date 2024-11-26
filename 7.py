import rsa

# Generate keys
public_key, private_key = rsa.newkeys(2048)

with open('public.pem', 'wb') as f:
    f.write(public_key.save_pkcs1('PEM'))

with open('private.pem', 'wb') as f:
    f.write(private_key.save_pkcs1('PEM'))

# Sign the Doc
with open('samplepdf.pdf', 'rb') as f:
    data = f.read()

with open('private.pem', 'rb') as f:
    key = rsa.PrivateKey.load_pkcs1(f.read())

signature = rsa.sign(data, key, 'SHA-256')

with open('signature.txt', 'wb') as f:
    f.write(signature)


# Verify
with open('samplepdf.pdf','rb') as f:
    data = f.read()

with open('public.pem', 'rb') as puk:
    key = rsa.PublicKey.load_pkcs1(puk.read())

with open('signature.txt', 'rb') as sf:
    signature = sf.read()

verify_file = rsa.verify(data, signature, key)
print(verify_file)