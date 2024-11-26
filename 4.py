import hashlib
import requests

def hash_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1_hash


def isPwned(password):
    sha1_hash = hash_password(password)
    first_five_chars = sha1_hash[:5]
    remaining_chars = sha1_hash[5:]

    url = f'https://api.pwnedpasswords.com/range/{first_five_chars}'
    response = requests.get(url)
    if response.status_code != 200:
        return False

    for line in response.text.splitlines():
        hash, count = line.split(':')
        if hash == remaining_chars:
            return int(count)
    return False

def main():
    input_file = "credentials.txt"

    try:
        with open(input_file, 'r') as file:
            for line in file:
                username, password = line.strip().split(",")
                count = isPwned(password)
                if count > 0:
                    print(f"WARNING: {username}'s password has been leaked {count} times!")
                else:
                    print(f"{username}'s password is safe (not found in the database).")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    main()

