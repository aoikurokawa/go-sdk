import typing

from solders.pubkey import Pubkey

class Operator:
    """
    The Operator account stores global information for a particular operator
    including the admin, voter, and the number of NCN and vault accounts.

    ...

    Attributes
    ----------
    base : Pubkey
        The base pubkey used as a seed for the PDA
    
    admin : Pubkey
        The admin pubkey

    ncn_admin : Pubkey
        The NCN admin can add and remove support for NCNs in the restaking protocol

    vault_admin : Pubkey
        The vault admin can add and remove support for vaults in the restaking protocol

    delegate_admin : Pubkey
        The delegate admin can delegate assets from the operator
    
    delegate_admin : Pubkey
        The delegate admin of the NCN

    metadata_admin : Pubkey
        ( For future use ) Authority to update the operators's metadata
        
    weight_table_admin : Pubkey
        The voter pubkey can be used as the voter for signing transactions for interacting
        with various NCN programs. NCNs can also opt for their own signing infrastructure.
    
    voter : Pubkey
        Admin in charge of of any on-chain programs related to the NCN
    
    index : int
        The operator index

    ncn_count : int
        The number of NcnOperatorTickets associated with the operator.
        Helpful for indexing all available OperatorNcnTickets.

    vault_count : int
        The number of NcnVaultTickets associated with the operator.
        Helpful for indexing all available OperatorVaultTickets.

    operator_fee_bps : int
        The operator fee in basis points

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
    base: Pubkey
    admin: Pubkey
    ncn_admin: Pubkey
    vault_admin: Pubkey
    delegate_admin: Pubkey
    metadata_admin: Pubkey
    index: int
    ncn_count: int
    vault_count: int
    operator_fee_bps: int
    bump: int

    # Initialize a Ncn instance with required attributes
    def __init__(self, base: Pubkey, admin: Pubkey, ncn_admin: Pubkey, vault_admin: Pubkey, delegate_admin: Pubkey, metadata_admin: Pubkey, voter: Pubkey, index: int, ncn_count: int, vault_count: int, operator_fee_bps: int, bump: int):
        self.base = base
        self.admin = admin
        self.ncn_admin = ncn_admin
        self.vault_admin = vault_admin
        self.delegate_admin = delegate_admin
        self.metadata_admin = metadata_admin
        self.voter = voter
        self.index = index
        self.ncn_count = ncn_count
        self.vault_count = vault_count
        self.operator_fee_bps = operator_fee_bps
        self.bump = bump

    # Display Ncn
    def __str__(self):
        return (
            f"NCN(\n"
            f"  base={self.base},\n"
            f"  admin={self.admin},\n"
            f"  ncn_admin={self.ncn_admin},\n"
            f"  vault_admin={self.vault_admin},\n"
            f"  delegate_admin={self.delegate_admin},\n"
            f"  metadata_admin={self.metadata_admin},\n"
            f"  voter={self.voter},\n"
            f"  index={self.index},\n"
            f"  ncn_count={self.ncn_count},\n"
            f"  vault_count={self.vault_count},\n"
            f"  operator_fee_bps={self.operator_fee_bps},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "Operator":
        """Deserializes bytes into a Operator instance."""
        
        # Define offsets for each field
        offset = 0
        offset = 8

        base = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        ncn_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        vault_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        delegate_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        metadata_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        voter = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        ncn_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        vault_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        operator_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return Operator(
            base,
            admin,
            ncn_admin,
            vault_admin,
            delegate_admin,
            metadata_admin,
            voter,
            index,
            ncn_count,
            vault_count,
            operator_fee_bps,
            bump
        )

    @staticmethod
    def seeds(base: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"operator", bytes(base)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, base: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = Operator.seeds(base)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
