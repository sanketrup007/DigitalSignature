from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Read private key from file
with open('private_key.pem', 'rb') as f:
    private_key_pem = f.read()

private_key = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
    backend=default_backend()
)

# Read hashed message from file
with open('hashed_message.txt', 'rb') as f:
    hashed_message = f.read()

# Sign the hashed message
signature = private_key.sign(
    hashed_message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Well done!\n\nYou created a signature you always wanted\nCheck you folder")
# Write signature to file
with open('signature.bin', 'wb') as f:
    f.write(signature)
