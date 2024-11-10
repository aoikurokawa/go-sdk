from solders.pubkey import Pubkey

from restakingpy.restaking_client import RestakingClient

RPC_URL = "https://api.devnet.solana.com"
RESTAKING_PROGRAM_ID = "RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q"
VAULT_PROGRAM_ID = "Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8"
# NCN_PUBKEY = "8gWHpwRmM3K4kAZEZV2jdERBjf1KtKWDc7kHsPpXsgLB"
NCN_PUBKEY = "8gWHpwRmM3K4kAZEZV2jdERBjf1KtKWDc7kHsPpXsgLB"
OPERATOR_PUBKEY = "2Uit7hCcTnMFFDYszysxMMWYuh2s2r6UfQAw8D1T5PNW"

def main():
    # Replace with your actual config account public key
    restaking_program_id = Pubkey.from_string(RESTAKING_PROGRAM_ID)
    vault_program_id = Pubkey.from_string(VAULT_PROGRAM_ID)
    ncn_pubkey = Pubkey.from_string(NCN_PUBKEY)
    operator_pubkey = Pubkey.from_string(OPERATOR_PUBKEY)

    # Initialize the RPC client
    client = RestakingClient(RPC_URL, restaking_program_id, vault_program_id)

    # Fetch and print the config account
    ncn_account = client.get_ncn_operator_state(ncn_pubkey, operator_pubkey)
    if ncn_account:
        print("NCNOperatorState Account:", ncn_account)
    else:
        print("Failed to retrieve config account.")

if __name__ == "__main__":
    main()
