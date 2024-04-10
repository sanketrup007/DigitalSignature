from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load the private key
with open('private_key.pem', 'rb') as f:
    private_key_pem = f.read()
    private_key = serialization.load_pem_private_key(private_key_pem, password=None, backend=default_backend())

# Load the ciphertext
with open('ciphertext.bin', 'rb') as f:
    ciphertext = f.read()

# Decrypt the message
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(plaintext.decode())
