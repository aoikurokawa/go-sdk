// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import {ERC721} from "../src/ERC721.sol";

contract ERC721Test is Test {
    ERC721 erc721;
    address alice = address(0x1);
    address bob = address(0x2);

    function testMintToken() public {
        erc721 = new ERC721();
        erc721._mint(alice, 0);
        address _ownerOf = erc721.ownerOf(0);
        assertEq(alice, _ownerOf);
    }

    function testTransferFrom() public {
        erc721 = new ERC721();
        erc721._mint(alice, 0);

        vm.startPrank(alice);
        erc721.safeTransferFrom(alice, bob, 0);
        vm.stopPrank();

        address _ownerOf = erc721.ownerOf(0);
        assertEq(bob, _ownerOf);
    }
}
