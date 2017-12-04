from Block import Block
import datetime as date
class Doctor:

    def __init__(self, mediator):
        self.BlockChain = []
        self.mediator = mediator
        self.subscribe()

    def subscribe(self):
        """
        Subscribes instance to defined mediator
        """
        self.mediator.Subscribers.append(self)

    def add_block(self):
        """
        adds block to blockchain, through mediator
        """
        self.mediator.add_block(self.mediator.create_block())

    def create_genesis_block(self):
        """
        Creates initial block in blockchain
        """
        return Block(index=0, timestamp=str(date.datetime.now()), header="Genesis Block", data="In the beginning God created the heavens and the earth.", previous_hash="0")

    def init_blockchain(self):
        """
        adds genesis block to chain
        """
        self.mediator.add_block(self.create_genesis_block())

    def print_chain(self):
        """
        prints blockchain
        """
        for block in self.BlockChain:
            print(block.header)
            print(block.data)
            print("hash: " + block.hash + "\n")
