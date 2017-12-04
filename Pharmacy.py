import json
import hashlib as hasher
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Padding
class Pharmacy:

    def __init__(self, mediator):
        self.BlockChain = []
        self.mediator = mediator
        self.subscribe()

    def subscribe(self):
        """
        Subscribes instance to defined mediator
        """
        self.mediator.Subscribers.append(self)

    def corrupt_block(self, index):
        try:
            self.BlockChain[index].header = "CORRUPTED."
            print("BlockChain Corrupted.")
        except Exception:
            print("Blockchain could not be corrupted.")

    def decrypt_chain(self):
        """
        decrypts and prints blockchain
        """
        password = "TzEQeLNDR~*r4<=L"
        key = hasher.sha256(password.encode('utf-8')).digest()
        for block in self.BlockChain:
            decryptor = AES.new(key, AES.MODE_CBC, IV=block.nonce)
            data = decryptor.decrypt(block.data)
            print(block.header)
            print(str(data) + "\n")
