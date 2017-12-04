from Block import Block
import datetime as date
from DataBuilder import DataBuilder
from CsvBuilder import CsvBuilder
from Pharmacy import Pharmacy
from Doctor import Doctor
from ChainMediator import ChainMediator

def main():

    # initializing csv builder to hold block hashes
    cb = CsvBuilder("output.csv")

    # initializing entites to share generated chain
    cm = ChainMediator()
    doctor = Doctor(cm)
    pharmacy = Pharmacy(cm)
    doctor.init_blockchain()

    while True:
        print("Options:")
        print("[1] Doctor: Write a prescription")
        print("[2] Doctor: View the blockchain (encrypted)")
        print("[3] Pharmacist: Fill a prescription (decrypted)")
        print("[4] Corrupt the blockchain")
        print("[5] Validate the blockchain")
        print("[6] Output blockchain hashes to CSV")
        print("[7] Clear blockchain hash CSV")
        print("[quit] exit program")

        decision = str(input())
        if decision == "quit":
            break

        # Doctor: Write a prescription (add a block to the chain)
        elif decision == "1":
            print("How many prescriptions (blocks) would you like to write? ")
            num_blocks = int(input())
            for i in range(num_blocks):
                doctor.add_block()

        # Doctor: View the blockchain (encrypted)
        elif decision == "2":
            doctor.print_chain()

        # Pharmacist: Fill a prescription (decrypted)
        elif decision == "3":
            pharmacy.decrypt_chain()

        # Corrupt the blockchain
        elif decision == "4":
            pharmacy.corrupt_block(1)

        # Validate the blockchain
        elif decision == "5":
            if(cm.validate_chain(pharmacy.BlockChain)):
                print("Blockchain is valid")
            else:
                print("BlockChain Corrupt. Resetting all blocks to Good Chain.")
                cm.fix_corrupt_chains()

        # write blockchain hashes to csv
        elif decision == "6":
            cb.write_to_csv()
            print("Output to",cb.file_path,"complete.")

        # clear hash csv file
        elif decision == "7":
            cb.clear_csv()
            print(cb.file_path,"cleared.")

        else:
            print("Please enter one of the valid options.")

if __name__ == "__main__":
    main()
