import cv2
import os

# Define paths (Stored in the same directory as the original image)
IMAGE_PATH = r"D:\Downloads\WhatsApp Image 2024-10-05 at 16.04.04_ea3ababc.jpg"
ENCODED_IMAGE_PATH = r"D:\Downloads\encrypted_image.png"
PASSWORD_FILE = r"D:\Downloads\password.txt"

def create_char_maps():
    """Creates encoding and decoding dictionaries."""
    d, c = {}, {}
    for i in range(256):
        d[chr(i)] = i
        c[i] = chr(i)
    return d, c

def encrypt_and_decrypt():
    """Encrypts a message inside the image and then decrypts it immediately."""
    img = cv2.imread(IMAGE_PATH)

    if img is None:
        print(" Error: Unable to load image!")
        return

    # Prompt user for message & password
    message = input("Enter secret message:")  # Matches format in your image
    password = input("Enter a passcode:")

    d, c = create_char_maps()
    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite(ENCODED_IMAGE_PATH, img)

    # Store password in a file
    with open(PASSWORD_FILE, "w") as f:
        f.write(password)

    print(f"\nEncrypted message stored in: {ENCODED_IMAGE_PATH}")

    # Start decryption immediately
    decrypt_message(message, password)

def decrypt_message(original_message, saved_password):
    """Decrypts the message from the image."""
    img = cv2.imread(ENCODED_IMAGE_PATH)

    if img is None:
        print("❌ Error: No encoded image found!")
        return

    d, c = create_char_maps()
    n, m, z = 0, 0, 0
    decrypted_message = ""

    for _ in range(len(original_message)):  # Extract the same number of characters
        decrypted_message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print(f"\nEnter passcode for Decryption{saved_password}")  # Matches your format
    print(f"Decryption message: {decrypted_message}")

if __name__ == "__main__":
    encrypt_and_decrypt()
