from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def encrypt_aes(input_string, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(input_string.encode('utf-8'), AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted.hex()

def decrypt_aes(encrypted_output, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(bytes.fromhex(encrypted_output)), AES.block_size)
    return decrypted.decode('utf-8')

def hash_string(input_string, algorithm):
    hashed_output = hashlib.new(algorithm, input_string.encode('utf-8')).hexdigest()
    return hashed_output

def save_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def main():
    # Get user input
    input_string = input("Enter the string to hash or encrypt: ")

    # Display the available algorithms
    print("Available algorithms:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")
    print("5. AES")

    # Get user selection for the algorithm
    option = input("Select an algorithm (1-5): ")

    if option == "1":
        algorithm = 'md5'
    elif option == "2":
        algorithm = 'sha1'
    elif option == "3":
        algorithm = 'sha256'
    elif option == "4":
        algorithm = 'sha512'
    elif option == "5":
        algorithm = 'AES'
    else:
        print("Invalid selection.")
        return

    if algorithm == 'AES':
        key = input("Enter the encryption key (16/24/32 bytes): ").encode('utf-8')
        try:
            key_length = len(key)
            if key_length not in [16, 24, 32]:
                raise ValueError("Incorrect AES key length ({0} bytes)".format(key_length))

            encrypted_output = encrypt_aes(input_string, key)
            decrypted_output = decrypt_aes(encrypted_output, key)
            print("Encrypted Output:", encrypted_output)
            print("Decrypted Output:", decrypted_output)
            description = input("Enter a description: ")
            data_to_save = f"Algorithm: {algorithm}\nDescription: {description}\nEncrypted Output: {encrypted_output}\nDecrypted Output: {decrypted_output}"
        except ValueError as e:
            print("Error:", str(e))
            return
    else:
        hashed_output = hash_string(input_string, algorithm)
        print("Hashed Output:", hashed_output)
        description = input("Enter a description: ")
        data_to_save = f"Algorithm: {algorithm}\nDescription: {description}\nHashed Output: {hashed_output}\n========================================"

    save_to_file("hashed.txt", data_to_save)
    print(f"Data saved to 'hashed.txt' for Algorithm: {algorithm}")

if __name__ == "__main__":
    main()
