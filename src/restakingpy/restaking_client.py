from solana.rpc.api import Client
from solders.pubkey import Pubkey
from restakingpy.accounts.restaking.config import Config
from restakingpy.accounts.restaking.ncn import Ncn
import typing

class RestakingClient:
    http_client: Client
    restaking_program_id: Pubkey
    vault_program_id: Pubkey

    def __init__(self, url: str, restaking_program_id: Pubkey, vault_program_id: Pubkey):
        self.http_client = Client(url)
        self.restaking_program_id = restaking_program_id
        self.vault_program_id = vault_program_id

    def get_restaking_config(self) -> typing.Optional[Config]:
        config_account_pubkey, _, _ = Config.find_program_address(self.restaking_program_id)

        try:
            response = self.http_client.get_account_info(config_account_pubkey)

            # Check if account data exists
            if response.value is None:
                print("Account data not found.")
                return None

            # Deserialize the account data
            # This assumes `data` in response is base64 encoded; decode and parse as needed
            data = response.value.data
            decoded_data = bytes(data)  # Convert data to bytes, as needed for decoding

            # # Deserialize into Config object (this part depends on how Config is stored)
            # # For example purposes, assume you have a method in Config to parse raw bytes
            config = Config.deserialize(decoded_data)

            return config
        
        except Exception as e:
            print("An error occured:", e)
            return None

    def get_ncn(self, ncn_pubkey: Pubkey) -> typing.Optional[Ncn]:
        try:
            response = self.http_client.get_account_info(ncn_pubkey)

            # Check if account data exists
            if response.value is None:
                print("Account data not found.")
                return None

            # Deserialize the account data
            # This assumes `data` in response is base64 encoded; decode and parse as needed
            data = response.value.data
            decoded_data = bytes(data)  # Convert data to bytes, as needed for decoding

            # # Deserialize into Config object (this part depends on how Config is stored)
            # # For example purposes, assume you have a method in Config to parse raw bytes
            config = Ncn.deserialize(decoded_data)

            return config
        
        except Exception as e:
            print("An error occured:", e)
            return None
