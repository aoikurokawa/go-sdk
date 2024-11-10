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

    # Initialize a Config instance with required attributes
    def __init__(self, admin: Pubkey, vaultProgram: Pubkey, ncnCount: int, operatorCount: int, epochLength: int, bump: int):
        self.admin = admin
        self.vaultProgram = vaultProgram
        self.ncnCount = ncnCount
        self.operatorCount = operatorCount
        self.epochLength = epochLength
        self.bump = bump

    # Display Config
    def __str__(self):
        return (
            f"Config(\n"
            f"  admin={self.admin},\n"
            f"  vaultProgram={self.vaultProgram},\n"
            f"  ncnCount={self.ncnCount},\n"
            f"  operatorCount={self.operatorCount},\n"
            f"  epochLength={self.epochLength},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    def deserialize(data: bytes) -> "Config":
        """Deserializes bytes into a Config instance."""
        
        # Define offsets for each field
        offset = 0

        # Unpack admin and vaultProgram (32 bytes each)
        admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        vaultProgram = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # NCN count
        ncnCount = int.from_bytes(data[offset:offset + 8])
        offset += 8
        
        # Operator count
        operatorCount = int.from_bytes(data[offset:offset + 8])
        offset += 8

        # Epoch length
        epochLength = int.from_bytes(data[offset:offset + 8])
        offset += 8

        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return Config(
            admin=admin,
            vaultProgram=vaultProgram,
            ncnCount=ncnCount,
            operatorCount=operatorCount,
            epochLength=epochLength,
            bump=bump,
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
