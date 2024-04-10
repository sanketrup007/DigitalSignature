from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

# Read public key from file
with open('public_key.pem', 'rb') as f:
    public_key_pem = f.read()

public_key = serialization.load_pem_public_key(
    public_key_pem,
    backend=default_backend()
)

# Read hashed message from file
with open('hashed_message.txt', 'rb') as f:
    hashed_message = f.read()

# Read signature from file
with open('signature.bin', 'rb') as f:
    signature = f.read()

try:
    public_key.verify(
        signature,
        hashed_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.\nI know you have changed nothing. Such a good boy/girl!")
except InvalidSignature:
    print("I knew it! You would change.\n\nSignature is invalid.")
