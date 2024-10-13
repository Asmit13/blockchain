# blockchain_code.py

import web3
from web3 import Web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<YOUR_INFURA_PROJECT_ID>'))

# Create a contract interface
contract_abi = [
    # ... Contract ABI
]
contract_address = "0x<YOUR_CONTRACT_ADDRESS>"
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Generate random data
random_data = web3.sha3(text="Random data")

# Call a contract function with the random data
transaction_hash = contract.functions.storeData(random_data).transact()

# Wait for transaction confirmation
receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

print("Transaction hash:", transaction_hash)
print("Data stored on the blockchain:", receipt.logs[0].args.data)
