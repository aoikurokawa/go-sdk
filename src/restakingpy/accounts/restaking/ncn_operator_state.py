import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class NcnOperatorState:

    discriminator: typing.ClassVar = 4
    ncn: Pubkey
    operator:Pubkey
    index: int
    ncn_opt_in_state: SlotToggle
    operator_opt_in_state: SlotToggle
    bump: int

    # Initialize a NcnOperatorState instance with required attributes
    def __init__(self, ncn: Pubkey, operator: Pubkey, index: int, ncn_opt_in_state: SlotToggle, operator_opt_in_state: SlotToggle, bump: int):
        self.ncn = ncn
        self.operator = operator
        self.index = index
        self.ncn_opt_in_state = ncn_opt_in_state
        self.operator_opt_in_state = operator_opt_in_state
        self.bump = bump

    # Display Config
    def __str__(self):
        return (
            f"NcnOperatorState(\n"
            f"  ncn={self.ncn},\n"
            f"  operator={self.operator},\n"
            f"  index={self.index},\n"
            f"  ncn_opt_in_state={self.ncn_opt_in_state},\n"
            f"  operator_opt_in_state={self.operator_opt_in_state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "NcnOperatorState":
        """Deserializes bytes into a NcnOperatorState instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        operator = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        

        ncn_opt_in_state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        operator_opt_in_state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return NcnOperatorState(
            ncn,
            operator,
            index,
            ncn_opt_in_state,
            operator_opt_in_state,
            bump
        )

    @staticmethod
    def seeds(ncn: Pubkey, operator: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"ncn_operator_state", bytes(ncn), bytes(operator)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, ncn: Pubkey, operator: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = NcnOperatorState.seeds(ncn, operator)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
