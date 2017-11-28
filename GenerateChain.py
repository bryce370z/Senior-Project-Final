from Block import Block
import datetime as date
from DataBuilder import DataBuilder
from CsvBuilder import CsvBuilder
from Pharmacy import Pharmacy
from Doctor import Doctor
from ChainMediator import ChainMediator

def genesis_block():
    """
    Creates initial block in blockchain
    """
    return Block(index=0, timestamp=str(date.datetime.now()), header="Genesis Block", data="In the beginning God created the heavens and the earth.", previous_hash="0")

def next_block(last_block):
    """
    Creates next block in blockchain
        args:
            last_block: the previous block in the blockchain
    """
    index = last_block.index + 1
    timestamp = str(date.datetime.now())
    header = "BLOCK: " + str(index)
    db = DataBuilder()
    data = db.build_data()
    last_block_hash = last_block.hash
    return Block(index=index, timestamp=timestamp, header=header, data=data, previous_hash=last_block_hash)

def main():
    # outputting hashes to CSV for analysis
    cb = CsvBuilder("output.csv")
    print("would you like to clear the csv output file, before taking in the next list of hashes? Y/N: ")
    choice = str(input())
    if choice == "Y" or choice == "y":
        cb.clear_csv()

    # initializing entites to share generated chain
    cm = ChainMediator()
    doctor = Doctor(cm)
    pharmacy = Pharmacy(cm)
    doctor.add_block(genesis_block())

    while True:
        print("Options:")
        print("[1] Doctor: Write a prescription")
        print("[2] Doctor: View the blockchain (encrypted)")
        print("[3] Pharmacist: Fill a prescription (decrypted)")
        print("[4] Corrupt the blockchain")
        print("[5] Validate the blockchain")
        print("[6] Output blockchain to CSV")
        print("[quit] exit program")

        decision = str(input())
        if decision == "quit":
            break

        # Doctor: Write a prescription (add a block to the chain)
        elif decision == "1":
            print("How many prescriptions (blocks) would you like to write? ")
            num_blocks = int(input())
            for i in range(1, num_blocks + 1):
                new_block = next_block(doctor.BlockChain[i - 1])
                doctor.add_block(new_block)
                cb.add_data(str(new_block.hash))
                # print(str(new_block.hash) + str(new_block.index))

        # Doctor: View the blockchain (encrypted)
        elif decision == "2":
            doctor.print_chain()

        # Pharmacist: Fill a prescription (decrypted)
        elif decision == "3":
            pharmacy.decrypt_chain()

        # Corrupt the blockchain
        elif decision == "4":
            pharmacy.corrupt_block(1)
            print("Blockchain corrupted.")

        # Validate the blockchain
        elif decision == "5":
            if(cm.validate_chain(pharmacy.BlockChain)):
                print("Blockchain is valid")
            else:
                print("BlockChain Corrupt. Resetting all blocks to Good Chain.")
                cm.fix_corrupt_chains()

        # write blockchain to csv
        elif decision == "6":
            cb.write_to_csv()
            print("Output complete.")
            
        else:
            print("Please enter one of the valid options.")

if __name__ == "__main__":
    main()
