import os
from cryptography.hazmat.primitives import hashes
import base64

# Message to be signed
message = b"Hello, world!"

# Hash the message using SHA-256
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
hash_of_message = digest.finalize()

print("Going right on track!\n\nHere are the hash of message- Hello, world! in different formats:\n") 

# Print the hashed message in hex format
print("Hashed Message (hex):", hash_of_message.hex())

# Print the hashed message in integer format
print("Hashed Message (Integer):", int.from_bytes(hash_of_message, byteorder='big'))

# Print the hashed message in binary format
print("Hashed Message (Binary):", ''.join(format(byte, '08b') for byte in hash_of_message))

# Print the hashed message in Base64 format
print("Hashed Message (Base64):", base64.b64encode(hash_of_message).decode('utf-8'))

# Save the hashed message to a file
hashed_message_path = os.path.join(os.getcwd(), 'hashed_message.txt')
with open(hashed_message_path, 'wb') as f:
    f.write(hash_of_message)
