import hashlib
import os

HASH_FILE = "hashes.txt"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()

def save_hash(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    file_hash = calculate_hash(file_path)

    with open(HASH_FILE, "a") as file:
        file.write(file_path + ":" + file_hash + "\n")

    print("Hash saved successfully.")

def verify_hash(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if not os.path.exists(HASH_FILE):
        print("No saved hashes found.")
        return

    current_hash = calculate_hash(file_path)

    with open(HASH_FILE, "r") as file:
        saved_hashes = file.readlines()

    for line in saved_hashes:
        saved_file, saved_hash = line.strip().split(":")

        if saved_file == file_path:
            if current_hash == saved_hash:
                print("File integrity verified. No changes detected.")
            else:
                print("WARNING: File has been modified!")
            return

    print("This file was not found in the saved hash database.")

print("File Integrity Checker")
print("1. Save file hash")
print("2. Verify file integrity")

choice = input("Choose option 1 or 2: ")
file_path = input("Enter file path: ")

if choice == "1":
    save_hash(file_path)
elif choice == "2":
    verify_hash(file_path)
else:
    print("Invalid choice.")