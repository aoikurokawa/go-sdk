import typing
from solders.pubkey import Pubkey

class Config:
    discriminator: typing.ClassVar = 0
    admin: Pubkey
    vaultProgram:Pubkey
    ncnCount: int
    operatorCount: int
    epochLength: int
    bump: int
    reserved: list[int]

    # Initialize a Config instance with required attributes
    def __init__(self, admin: Pubkey, vaultProgram: Pubkey, ncnCount: int, operatorCount: int, epochLength: int, bump: int, reserved: list[int]):
        self.admin = admin
        self.vaultProgram = vaultProgram
        self.ncnCount = ncnCount
        self.operatorCount = operatorCount
        self.epochLength = epochLength
        self.bump = bump
        self.reserved = reserved

    @staticmethod
    def seeds() -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"config"]
    
    @staticmethod
    def find_program_address(program_id: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = Config.seeds()
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
