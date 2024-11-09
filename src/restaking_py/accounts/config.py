import typing
from solders.pubkey import Pubkey

class Config:
    discriminator: typing.ClassVar = 0
    admin: Pubkey
    vaultProgram:
    ncnCount:
    operatorCount:
    epochLength:
    bump: 
    reserved: 

    def __init__(self, ):
