from bitcoinaddress import Wallet

# Open the file containing private keys
with open('infinitesha.txt', 'r') as file:
    private_keys = file.readlines()

# Open the output file to save wallet information
with open('saved.txt', 'w') as output_file:
    for key in private_keys:
        key = key.strip()  # Remove any extra whitespace
        wallet = Wallet(key)
        output_file.write(str(wallet) + '\n')
        print(wallet)

