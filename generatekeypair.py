import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize the private key to PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Generate the corresponding public key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the keys to files
private_key_path = os.path.join(os.getcwd(), 'private_key.pem')
public_key_path = os.path.join(os.getcwd(), 'public_key.pem')

with open(private_key_path, 'wb') as f:
    f.write(private_key_pem)

with open(public_key_path, 'wb') as f:
    f.write(public_key_pem)

print("Good start!\n\nBoth Private and Public keys are generated. Check your folder")
