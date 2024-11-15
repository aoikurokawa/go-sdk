import typing

from solders.pubkey import Pubkey

class Config:

    discriminator: typing.ClassVar = 1
    admin: Pubkey
    restaking_program:Pubkey
    epoch_length: int
    num_vaults: int
    deposit_withdrawal_fee_cap_bps: int
    fee_rate_of_change_bps: int
    fee_bump_bps: int
    program_fee_bps: int
    program_fee_wallet: Pubkey
    fee_admin: Pubkey
    bump: int

    # Initialize a Config instance with required attributes
    def __init__(self, admin: Pubkey, restaking_program: Pubkey, epoch_length: int, num_vaults: int, deposit_withdrawal_fee_cap_bps: int, fee_rate_of_change_bps: int, fee_bump_bps: int, program_fee_bps: int, program_fee_wallet: Pubkey, fee_admin: Pubkey, bump: int):
        self.admin = admin
        self.restaking_program = restaking_program
        self.epoch_length = epoch_length
        self.num_vaults = num_vaults
        self.deposit_withdrawal_fee_cap_bps = deposit_withdrawal_fee_cap_bps
        self.fee_rate_of_change_bps = fee_rate_of_change_bps
        self.fee_bump_bps = fee_bump_bps
        self.program_fee_bps = program_fee_bps
        self.program_fee_wallet = program_fee_wallet
        self.fee_admin = fee_admin
        self.bump = bump

    # Display Config
    def __str__(self):
        return (
            f"Config(\n"
            f"  admin={self.admin},\n"
            f"  restaking_program={self.restaking_program},\n"
            f"  epoch_length={self.epoch_length},\n"
            f"  num_vaults={self.num_vaults},\n"
            f"  deposit_withdrawal_fee_cap_bps={self.deposit_withdrawal_fee_cap_bps},\n"
            f"  fee_rate_of_change_bps={self.fee_rate_of_change_bps},\n"
            f"  fee_bump_bps={self.fee_bump_bps},\n"
            f"  program_fee_bps={self.program_fee_bps},\n"
            f"  program_fee_wallet={self.program_fee_wallet},\n"
            f"  fee_admin={self.fee_admin},\n"
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

        restaking_program = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Epoch length
        epoch_length = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Number of vaults
        num_vaults = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        deposit_withdrawal_fee_cap_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        fee_rate_of_change_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        fee_bump_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        program_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        program_fee_wallet = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        fee_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        
        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return Config(
            admin,
            restaking_program,
            epoch_length,
            num_vaults,
            deposit_withdrawal_fee_cap_bps,
            fee_rate_of_change_bps,
            fee_bump_bps,
            program_fee_bps,
            program_fee_wallet,
            fee_admin,
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
