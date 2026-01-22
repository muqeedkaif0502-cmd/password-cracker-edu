import hashlib

password = input("Enter a password to hash: ")

import hashlib

password = input("Enter a password to hash: ")

hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.hexdigest()

with open("hashed.txt", "w") as file:
    file.write(hashed_password)

print("Password hashed and saved successfully.")
import hashlib

# Read stored hash
with open("hashed.txt", "r") as file:
    target_hash = file.read()

# Open wordlist
123456
password
hello
welcome
letmein

with open("wordlist.txt", "r") as file:
    words = file.readlines()

found = False

for word in words:
    word = word.strip()
    word_hash = hashlib.sha256(word.encode()).hexdigest()

    print(f"Trying: {word}")

    if word_hash == target_hash:
        print("\nPassword CRACKED!")
        print("Password is:", word)
        found = True
        break

if not found:
    print("\nPassword not found in wordlist.")
# Educational Password Cracker

## Description
# This project demonstrates how weak passwords can be cracked using a dictionary attack
# in a controlled environment.

## Purpose
