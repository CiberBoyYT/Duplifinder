import os
import hashlib

def get_file_hash(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def find_duplicates(directory):
    file_hashes = {}
    duplicates = []
    for foldername, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_hash = get_file_hash(file_path)

            if file_hash in file_hashes:
                duplicates.append((file_hashes[file_hash], file_path))
            else:
                file_hashes[file_hash] = file_path
    if duplicates:
        print("Duplicate files found:")
        for original, duplicate in duplicates:
            print(f"Original: {original}\nDuplicate: {duplicate}\n")
    else:
        print("No duplicates found.")

path_select = input("type the path to find possible duplicate files: ")
find_duplicates(path_select)
