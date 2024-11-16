from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.ncn import Ncn


def test_deserialize():
    ncn_bytes = bytes([2, 0, 0, 0, 0, 0, 0, 0, 61, 154, 94, 164, 0, 101, 24, 152, 129, 67, 58, 9, 252, 91, 145, 10, 178, 241, 129, 94, 40, 186, 22, 212, 47, 181, 94, 167, 71, 196, 199, 109, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])    
    ncn = Ncn.deserialize(ncn_bytes)
    
    assert ncn.base == Pubkey.from_string("59UPuSh1Ex2ZYwjy6soqjqd8Ka8CkxhmfvuDJVa1ZxxU")
    assert ncn.admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.operator_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.vault_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.slasher_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.delegate_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.metadata_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.weight_table_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.ncn_program_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert ncn.index == 0
    assert ncn.operator_count == 1
    assert ncn.vault_count == 1
    assert ncn.slasher_count == 0
    assert ncn.bump == 254

