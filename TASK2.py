import re

def check_ethereum(address):
    
    ethereum_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')

    if ethereum_address_pattern.match(address):
        return True
    else:
        return False


ethereum_address = input("Enter your Ethereum Address:")


result = check_ethereum(ethereum_address)

print(result)

