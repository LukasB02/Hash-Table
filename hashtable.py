def hash(key):
    hash = 0
    for char in key:
        hash = (hash * 31 + ord(char)) % 2003
    return hash