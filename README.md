# Simple BNB Balance Checker

The simplest script that checks balances in the BNB SmartChain network using the BSCScan API.

# Setup

To import wallet addresses, you need to paste them into `wallet_addresses`. (ENS and other domains are not supported yet)

example: 
```sh
wallet_addresses = [
    '0xd3eA09Fe79AE41DA92f7048eBaA69932D706ed34',
    '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
]
```

To import a token, you need to paste the contract address into `token_address`

example: 
```sh
token_address = '0x55d398326f99059fF775485246999027B3197955' #USDT
```
