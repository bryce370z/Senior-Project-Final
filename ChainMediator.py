from Doctor import Doctor
from Pharmacy import Pharmacy
import copy
class ChainMediator:

    def __init__(self):
        self.GoodChain = []
        self.Subscribers = []

    def add_block(self, new_block):
        """
        Adds Block to all Subscriber's blockchains
            args:
                new_block: new block to be appended to blockchain
        """
        for sub in self.Subscribers:
            if(self.validate_chain(sub.BlockChain)):
                sub.BlockChain.append(new_block)
            else:
                print("Cannot add new block. Current chain is corrupt")
                self.fix_corrupt_chains()
                return
        self.GoodChain.append(copy.copy(new_block))

    def fix_corrupt_chains(self):
        # print(len(self.GoodChain))
        # print(len(self.Subscribers[0].BlockChain))
        for sub in self.Subscribers:
            sub.BlockChain = copy.deepcopy(self.GoodChain)
            print('Resetting Chain')

    def validate_chain(self, BlockChain):
        """
        Finds any corrupt blocks in the BlockChain
            args:
                BlockChain: blockchain to be validated
            return: boolean
        """
        for i in range(len(BlockChain)):
            current_block = BlockChain[i]
            old_hash = current_block.hash
            new_hash = current_block.hash_block()
            if old_hash != new_hash:
                print("BLOCK: " + str(current_block.index) + " is corrupt.")
                # print(str(current_block.data) + "\n")
                # print(current_block.hash)
                return False
        return True
