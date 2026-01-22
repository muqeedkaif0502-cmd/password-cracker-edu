import hashlib

password = input("Enter a password to hash: ")

hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.hexdigest()

with open("hashed.txt", "w") as file:
    file.write(hashed_password)

print("Password hashed and saved successfully.")
