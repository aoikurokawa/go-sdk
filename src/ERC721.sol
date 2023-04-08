// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

interface IERC165 {
    function supportsInterface(bytes4 interfaceID) external view returns (bool);
}

interface IERC721 is IERC165 {
    function balanceOf(address owner) external view returns (uint balance);

    function ownerOf(uint tokenId) external view  returns (address owner);

    function safeTransferFrom(address from, address to, uint tokenId) external;

    function safeTransferFrom(address from, address to, uint tokenId, bytes calldata data) external;

    function transferFrom(address from, address to, uint tokenId) external;

    function approve(address to, uint tokenId) external;

    function getApproved(uint tokenId) external view returns (address operator);

    function setApprovalForAll(address operator, bool _approved)  external;

    // function isApprovedForAll(address owner, address operator) external view returns (bool);
} 

interface IERC721Receiver {
    function onERC721Received(address operator, address from, uint tokenId, bytes calldata data) external returns (bytes4);
}

contract ERC721 is IERC721 {
    event Transfer(address indexed from, address indexed to, uint indexed id);
    event Approval(address indexed owner, address indexed spender, uint indexed id);
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);
    
    // Mapping from tokenID to owner address
    mapping(uint => address) internal _ownerOf;

    // Mapping owner address to token count
    mapping(address => uint) internal _balanceOf;

    // Mapping from token ID to approved address
    mapping(uint => address) internal _approvals;

    // Mapping from owner to operator approvals
    mapping(address => mapping(address =>  bool)) public isApprovedForAll;

    function supportsInterface(bytes4 interfaceId) external pure returns (bool) {
        return 
            interfaceId == type(IERC721).interfaceId ||
            interfaceId == type(IERC165).interfaceId;
    }

    function ownerOf(uint id) external view returns (address owner) {
        owner = _ownerOf[id];
        require(owner != address(0), "token doesn't exist");
    }

    function balanceOf(address owner) external view returns (uint) {
        require(owner != address(0), "owner = zero address");
        return _balanceOf[owner];
    }

    function safeTransferFrom(address from, address to, uint tokenId) external {
        transferFrom(from, to, tokenId);

        require(
            to.code.length == 0 ||
                IERC721Receiver(to).onERC721Received(msg.sender, from, tokenId, "") == 
                IERC721Receiver.onERC721Received.selector,
            "unsafe recipient"
        );
    }

    function safeTransferFrom(address from, address to, uint tokenId, bytes calldata data) external {
        transferFrom(from, to, tokenId);

        require(
            to.code.length == 0 ||
                IERC721Receiver(to).onERC721Received(msg.sender, from, tokenId, data) == 
                IERC721Receiver.onERC721Received.selector,
            "unsafe recipient"
        );
    }

    function transferFrom(address from, address to, uint tokenId) public {
        require(from == _ownerOf[tokenId], "from != owner");
        require(to != address(0), "transfer to address zero");

        require(_isApprovedOrOwner(from, msg.sender, tokenId), "not authorized");

        _balanceOf[from]--;
        _balanceOf[to]++;
        _ownerOf[tokenId] = to;

        delete _approvals[tokenId];

        emit Transfer(from, to, tokenId);
    }

    function approve(address to, uint tokenId) external {
        address owner = _ownerOf[tokenId];
        require(
            msg.sender == owner || isApprovedForAll[owner][msg.sender],
            "not authorized"
        );

        _approvals[tokenId] = to;

        emit Approval(owner, to, tokenId);
    }

    function getApproved(uint tokenId) external view returns (address operator) {
        require(_ownerOf[tokenId] != address(0), "token doesn't exist");
        return _approvals[tokenId];
    }

    function setApprovalForAll(address operator, bool _approved)  external {
        isApprovedForAll[msg.sender][operator] = _approved;
        emit ApprovalForAll(msg.sender, operator, _approved);
    }

    // function isApprovedForAll(address owner, address operator) external view returns (bool);

    function _isApprovedOrOwner(address owner, address spender, uint id) internal view returns (bool) {
        return (spender == owner || isApprovedForAll[owner][spender] || spender == _approvals[id]);
    }

    function _mint(address to, uint id) external {
        require(to != address(0), "mint to zero address");
        require(_ownerOf[id] == address(0), "already minted");

        _balanceOf[to]++;
        _ownerOf[id] = to;

        emit Transfer(address(0), to, id);
    }

    function _burn(uint id) external {
        address owner = _ownerOf[id];
        require(owner != address(0), "not minted");

        _balanceOf[owner] != 1;

        delete _ownerOf[id];
        delete _approvals[id];

        emit Transfer(owner, address(0), id);
    }
}

// contract MyNFT is ERC721 {
//     function mint(address to, uint id) external {
//         _mint(to, id);
//     }
// 
//     function burn(uint id) external {
//         require(msg.sender == _ownerOf[id], "not owner");
//         _burn(id);
//     }
// }
