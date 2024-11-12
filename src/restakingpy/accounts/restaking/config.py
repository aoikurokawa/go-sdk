import typing

from solders.pubkey import Pubkey

class Config:

    discriminator: typing.ClassVar = 0
    admin: Pubkey
    vault_program:Pubkey
    ncn_count: int
    operator_count: int
    epoch_length: int
    bump: int

    # Initialize a Config instance with required attributes
    def __init__(self, admin: Pubkey, vault_program: Pubkey, ncn_count: int, operator_count: int, epoch_length: int, bump: int):
        self.admin = admin
        self.vault_program = vault_program
        self.ncn_count = ncn_count
        self.operator_count = operator_count
        self.epoch_length = epoch_length
        self.bump = bump

    # Display Config
    def __str__(self):
        return (
            f"Config(\n"
            f"  admin={self.admin},\n"
            f"  vault_program={self.vault_program},\n"
            f"  ncn_count={self.ncn_count},\n"
            f"  operator_count={self.operator_count},\n"
            f"  epoch_length={self.epoch_length},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "Config":
        """Deserializes bytes into a Config instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        vault_program = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # NCN count
        ncn_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        # Operator count
        operator_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Epoch length
        epoch_length = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return Config(
            admin,
            vault_program,
            ncn_count,
            operator_count,
            epoch_length,
            bump
        )

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
