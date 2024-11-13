import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class OperatorVaultTicket:
    """

    ...

    Attributes
    ----------
    operator : Pubkey
        The operator account
    
    vault : Pubkey
        The vault pubkey

    index : int
        The operator index

    state : SlotToggle
        The slot toggle

    bump : int
        The bump seed for the PDA


    Methods
    -------
    deserialize(data: bytes)
        Deserialize the account data to NCN struct

    seeds(base: Pubkey):
        Returns the seeds for the PDA

    find_program_address(program_id: Pubkey, base: Pubkey):
        Find the program address for the NCN account
    """

    discriminator: typing.ClassVar = 3
    operator: Pubkey
    vault: Pubkey
    index: int
    state: SlotToggle
    bump: int

    # Initialize a Operator instance with required attributes
    def __init__(self, operator: Pubkey, vault: Pubkey, index: int, state: SlotToggle, bump: int):
        self.operator = operator
        self.vault = vault
        self.index = index
        self.state = state
        self.bump = bump

    # Display OperatorVaultTicket
    def __str__(self):
        return (
            f"OperatorVaultTicket(\n"
            f"  operator={self.operator},\n"
            f"  vault={self.vault},\n"
            f"  index={self.index},\n"
            f"  state={self.state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "OperatorVaultTicket":
        """Deserializes bytes into a OperatorVaultTicket instance."""
        
        # Define offsets for each field
        offset = 0
        offset = 8

        operator = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32
        
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return OperatorVaultTicket(
            operator,
            vault,
            index,
            state,
            bump
        )

    @staticmethod
    def seeds(operator: Pubkey, vault: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"operator_vault_ticket", bytes(operator), bytes(vault)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, operator: Pubkey, vault: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = OperatorVaultTicket.seeds(operator, vault)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
