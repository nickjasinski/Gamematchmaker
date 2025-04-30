from user import User

class Block:
    def __init__(self, blockId: int, blockedId: int, blockerId: int):
        self.blockId = blockId
        self.blockedId = blockedId
        self.blockerId = blockerId

    def blockUser(self, user: User) -> bool:
        pass

    def unblockUser(self, user: User) -> bool:
        pass

    def retrieveBlocked(self) -> int:
        pass