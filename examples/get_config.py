from solders.pubkey import Pubkey
from restakingpy.restaking_client import RestakingClient

RPC_URL = "https://api.mainnet-beta.solana.com"
RESTAKING_PROGRAM_ID = "RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q"
VAULT_PROGRAM_ID = "Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8"

def main():
    # Replace with your actual config account public key
    restaking_program_id = Pubkey.from_string(RESTAKING_PROGRAM_ID)
    vault_program_id = Pubkey.from_string(VAULT_PROGRAM_ID)

    # Initialize the RPC client
    client = RestakingClient(RPC_URL, restaking_program_id, vault_program_id)

    # Fetch and print the config account
    # config_pubkey = Config.find_program_address(restaking_program_id)
    config_account = client.get_restaking_config()
    if config_account:
        print("Config Account:", config_account)
    else:
        print("Failed to retrieve config account.")

if __name__ == "__main__":
    main()