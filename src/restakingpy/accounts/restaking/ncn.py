from solders.pubkey import Pubkey
import typing

class Ncn:
    """
    The NCN manages the operators, vaults, and slashers associated with a network

    ...

    Attributes
    ----------
    base : Pubkey
        The base account used as a PDA seed
    
    admin : Pubkey
        The admin of the NCN

    operator_admin : Pubkey
        The operator admin of the NCN

    vault_admin : Pubkey
        The vault admin of the NCN

    slasher_admin : Pubkey
        The slasher admin of the NCN
    
    delegate_admin : Pubkey
        The delegate admin of the NCN

    metadata_admin : Pubkey
        ( For future use ) Authority to update the ncn's metadata\
        
    weight_table_admin : Pubkey
        The weight table admin of the NCN
    
    ncn_program_admin : Pubkey
        Admin in charge of of any on-chain programs related to the NCN
    
    index : int
        The index of the NCN

    operator_count : int
        Number of operator accounts associated with the NCN

    vault_count : int
        Number of vault accounts associated with the NCN

    slasher_count : int
        Number of slasher accounts associated with the NCN

    bump : int
        The bump seed for the PDA


    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    base: Pubkey
    admin: Pubkey
    operator_admin: Pubkey
    vault_admin: Pubkey
    slasher_admin: Pubkey
    delegate_admin: Pubkey
    metadata_admin: Pubkey
    weight_table_admin: Pubkey
    ncn_program_admin: Pubkey
    index: int
    operator_count: int
    vault_count: int
    slasher_count: int
    bump: int

    # Initialize a Ncn instance with required attributes
    def __init__(self, base: Pubkey, admin: Pubkey, operator_admin: Pubkey, vault_admin: Pubkey, slasher_admin: Pubkey, delegate_admin: Pubkey, metadata_admin: Pubkey, weight_table_admin: Pubkey, ncn_program_admin: Pubkey, index: int, operator_count: int, vault_count: int, slasher_count: int, bump: int):
        self.base = base
        self.admin = admin
        self.operator_admin = operator_admin
        self.vault_admin = vault_admin
        self.slasher_admin = slasher_admin
        self.delegate_admin = delegate_admin
        self.metadata_admin = metadata_admin
        self.weight_table_admin = weight_table_admin
        self.ncn_program_admin = ncn_program_admin
        self.index = index
        self.operator_count = operator_count
        self.vault_count = vault_count
        self.slasher_count = slasher_count
        self.bump = bump

    # Display Ncn
    def __str__(self):
        return (
            f"NCN(\n"
            f"  base={self.base},\n"
            f"  admin={self.admin},\n"
            f"  operator_admin={self.operator_admin},\n"
            f"  vault_admin={self.vault_admin},\n"
            f"  slasher_admin={self.slasher_admin},\n"
            f"  delegate_admin={self.delegate_admin},\n"
            f"  metadata_admin={self.metadata_admin},\n"
            f"  weight_table_admin={self.weight_table_admin},\n"
            f"  ncn_program_admin={self.ncn_program_admin},\n"
            f"  index={self.index},\n"
            f"  operator_count={self.operator_count},\n"
            f"  vault_count={self.vault_count},\n"
            f"  slasher_count={self.slasher_count},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "Ncn":
        """Deserializes bytes into a Config instance."""
        
        # Define offsets for each field
        offset = 0
        offset = 8

        # Unpack admin and vaultProgram (32 bytes each)
        base = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        operator_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        vault_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        slasher_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        delegate_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        metadata_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        weight_table_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        ncn_program_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # NCN count
        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        # Operator count
        operator_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Vault count
        vault_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Slasher count
        slasher_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return Ncn(
            base,
            admin,
            operator_admin,
            vault_admin,
            slasher_admin,
            delegate_admin,
            metadata_admin,
            weight_table_admin,
            ncn_program_admin,
            index,
            operator_count,
            vault_count,
            slasher_count,
            bump
        )

    @staticmethod
    def seeds(base: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"ncn", bytes(base)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, base: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = Ncn.seeds(base)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
