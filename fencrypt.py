from cryptography.fernet import Fernet
import hashlib

def generate_key():
    key = Fernet.generate_key()
    return key

def hash_content(content):
    hashed_content = hashlib.sha256(content).hexdigest()
    return hashed_content

def encrypt_file(file_path, encryption_key):
    # Read the file content
    with open(file_path, 'rb') as file:
        content = file.read()

    # Create the Fernet cipher object
    cipher = Fernet(encryption_key)

    # Encrypt the content
    encrypted_content = cipher.encrypt(content)

    # Write the encrypted content to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_content)

    print("File encrypted successfully.")

def decrypt_file(file_path, encryption_key):
    # Create the Fernet cipher object
    cipher = Fernet(encryption_key)

    # Read the encrypted file content
    with open(file_path, 'rb') as file:
        encrypted_content = file.read()

    # Decrypt the content
    decrypted_content = cipher.decrypt(encrypted_content)

    # Write the decrypted content to a new file
    decrypted_file_path = file_path + ".decrypted"
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_content)

    print("File decrypted successfully. Decrypted content saved to:", decrypted_file_path)

# Prompt the user for the file path
file_path = input("Enter the file path: ")

# Prompt the user for an action (encrypt or decrypt)
action = input("Enter 'enc' to encrypt the file or 'dec' to decrypt it: ")

if action == 'enc':
    # Generate a new encryption key
    encryption_key = generate_key()
    print("Generated encryption key:", encryption_key.decode())

    # Hash the file content
    with open(file_path, 'rb') as file:
        content = file.read()
        hashed_content = hash_content(content)
        
    print("Hashed content:", hashed_content)

    # Encrypt the file
    encrypt_file(file_path, encryption_key)

elif action == 'dec':
    # Prompt the user for the decryption key
    decryption_key = input("Enter the decryption key: ")

    # Decrypt the file
    decrypt_file(file_path, decryption_key)

else:
    print("Invalid action. Please choose either 'encrypt' or 'decrypt'.")
