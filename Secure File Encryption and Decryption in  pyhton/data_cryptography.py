from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'encryption_key.key'.")


def load_key():
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    return key


def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{filename}' has been encrypted.")


def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    print(f"File '{filename}' has been decrypted.")


if __name__ == "__main__":
    while True:
        print("\n=== Secure File Encryption and Decryption ===")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Terminate Program")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_to_encrypt = input("Enter the file name to encrypt: ")
            encrypt_file(file_to_encrypt)
        elif choice == "3":
            file_to_decrypt = input("Enter the file name to decrypt: ")
            decrypt_file(file_to_decrypt)
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")
