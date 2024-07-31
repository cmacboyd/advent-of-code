from hashlib import md5

secret_key = 'yzbqklnj'
i = 0
hash_value = md5(f'{secret_key}{i}'.encode())

while not hash_value.hexdigest().startswith('0'*5):
    i += 1
    hash_value = md5(f'{secret_key}{i}'.encode())

print(i)