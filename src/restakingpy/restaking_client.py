import typing

from solana.rpc.api import Client
from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.config import Config
from restakingpy.accounts.restaking.ncn import Ncn
from restakingpy.accounts.restaking.ncn_operator_state import NcnOperatorState
from restakingpy.accounts.restaking.ncn_vault_ticket import NcnVaultTicket

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

            if response.value is None:
                print("Account data not found.")
                return None

            data = response.value.data
            decoded_data = bytes(data)

            config = Config.deserialize(decoded_data)

            return config
        
        except Exception as e:
            print("An error occured:", e)
            return None

    def get_ncn(self, ncn_pubkey: Pubkey) -> typing.Optional[Ncn]:
        try:
            response = self.http_client.get_account_info(ncn_pubkey)

            if response.value is None:
                print("Account data not found.")
                return None

            data = response.value.data
            decoded_data = bytes(data)

            config = Ncn.deserialize(decoded_data)

            return config
        
        except Exception as e:
            print("An error occured:", e)
            return None

    def get_ncn_operator_state(self, ncn_pubkey: Pubkey, operator_pubkey: Pubkey) -> typing.Optional[NcnOperatorState]:
        ncn_operator_state_pubkey, _, _ = NcnOperatorState.find_program_address(self.restaking_program_id, ncn_pubkey, operator_pubkey)

        try:
            response = self.http_client.get_account_info(ncn_operator_state_pubkey)

            if response.value is None:
                print("Account data not found.")
                return None

            data = response.value.data
            decoded_data = bytes(data)

            ncn_operator_state = NcnOperatorState.deserialize(decoded_data)

            return ncn_operator_state
        
        except Exception as e:
            print("An error occured:", e)
            return None

    def get_ncn_vault_ticket(self, ncn_pubkey: Pubkey, vault_pubkey: Pubkey) -> typing.Optional[NcnVaultTicket]:
        ncn_vault_ticket_pubkey, _, _ = NcnVaultTicket.find_program_address(self.restaking_program_id, ncn_pubkey, vault_pubkey)

        try:
            response = self.http_client.get_account_info(ncn_vault_ticket_pubkey)

            if response.value is None:
                print("Account data not found.")
                return None

            data = response.value.data
            decoded_data = bytes(data)

            ncn_vault_ticket = NcnVaultTicket.deserialize(decoded_data)

            return ncn_vault_ticket
        
        except Exception as e:
            print("An error occured:", e)
            return None

