import requests

# Change to your API Key
API_KEY = 'YOUR_API_KEY'

# Wallet Addresses
wallet_addresses = [
    '0xA',
    '0xB',
]

# Token Address
token_address = '0x9879406C2EF6578CEB59009D64151Ef3f225830b'

def get_token_balances(wallet_addresses, token_address, api_key):
    balances = {}

    for address in wallet_addresses:
        url = 'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={}&address={}&tag=latest&apikey={}'.format(token_address, address, api_key)
        response = requests.get(url)
        data = response.json()

        if data['status'] == '1':
            balance = data['result']
            balances[address] = balance
        else:
            balances[address] = 'Error fetching balance'

    return balances

if __name__ == '__main__':
    token_balances = get_token_balances(wallet_addresses, token_address, API_KEY)

    for address, balance in token_balances.items():
        print(f'Address: {address}, Balance: {balance}')