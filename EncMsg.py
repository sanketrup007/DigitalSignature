from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Load the public key
with open('public_key.pem', 'rb') as f:
    public_key_pem = f.read()
    public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

# Encrypt the message
message = b"Hello, this is a secret message!"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save the ciphertext to a file
with open('ciphertext.bin', 'wb') as f:
    f.write(ciphertext)
    
with open('ciphertext.bin', 'rb') as file:
    # Read the contents of the file
    binary_data = file.read()

# Print the binary data
print("Try if you can read:\n\n",binary_data)
