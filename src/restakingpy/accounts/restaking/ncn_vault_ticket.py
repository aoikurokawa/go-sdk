import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class NcnVaultTicket:

    discriminator: typing.ClassVar = 6
    ncn: Pubkey
    vault:Pubkey
    index: int
    state: SlotToggle
    bump: int

    # Initialize a NcnVaultTicket instance with required attributes
    def __init__(self, ncn: Pubkey, vault: Pubkey, index: int, state: SlotToggle, bump: int):
        self.ncn = ncn
        self.vault = vault
        self.index = index
        self.state = state
        self.bump = bump

    # Display NcnVaultTicket
    def __str__(self):
        return (
            f"NcnVaultTicket(\n"
            f"  ncn={self.ncn},\n"
            f"  vault={self.vault},\n"
            f"  index={self.index},\n"
            f"  state={self.state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "NcnVaultTicket":
        """Deserializes bytes into a NcnVaultTicket instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return NcnVaultTicket(
            ncn,
            vault,
            index,
            state,
            bump
        )

    @staticmethod
    def seeds(ncn: Pubkey, vault: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"ncn_vault_ticket", bytes(ncn), bytes(vault)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, ncn: Pubkey, operator: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = NcnVaultTicket.seeds(ncn, operator)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
