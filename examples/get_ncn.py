from solders.pubkey import Pubkey

from restakingpy.restaking_client import RestakingClient

RPC_URL = "https://api.devnet.solana.com"
RESTAKING_PROGRAM_ID = "RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q"
VAULT_PROGRAM_ID = "Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8"
NCN_PUBKEY = "3gWkEDrg3DP5pYGfB53ic5HWL8yMWpJJ5Y4WoLuTX4dx"

def main():
    # Replace with your actual config account public key
    restaking_program_id = Pubkey.from_string(RESTAKING_PROGRAM_ID)
    vault_program_id = Pubkey.from_string(VAULT_PROGRAM_ID)
    ncn_pubkey = Pubkey.from_string(NCN_PUBKEY)

    # Initialize the RPC client
    client = RestakingClient(RPC_URL, restaking_program_id, vault_program_id)

    # Fetch and print the config account
    ncn_account = client.get_ncn(ncn_pubkey)
    if ncn_account:
        print("NCN Account:", ncn_account)
    else:
        print("Failed to retrieve config account.")

if __name__ == "__main__":
    main()
