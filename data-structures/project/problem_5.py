""""
Problem 5: Blockchain
Author: Annah Ramones

Version Date: March 18, 2021

Test Cases 2 and 3 are commented out because we expect them to throw ValueErrors
Please uncomment to test.

I am not including a test case for the same timestamp because, by design, my code handles that case
implicitly. The user just needs to input the data, and the code will record the timestamp when the user
inputs the data. This is done so that the user does not have the option to input a timestamp - in which case
they could input the same timestamp, or worse, input a timestamp that is before any of the other timestamps
in the BlockChain.

"""

import hashlib
from datetime import datetime as dt


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return("Timestamp: {}, Data: {}, Hash: {}, Previous Hash: {}"
               .format(self.timestamp, self.data, self.hash, self.previous_hash))


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        if data == "" or data is None:
            raise ValueError("Invalid data argument")

        if self.head is None:
            self.head = Block(dt.now(), data, 0)
            self.tail = self.head
            return

        self.tail.next = Block(dt.now(), data, self.tail.hash)
        self.tail = self.tail.next
        return

    def to_list(self):
        node = self.head
        output = []
        while node:
            output.append(node.__repr__())
            node = node.next
        return output


def main():
    # Test Case 1 - Basic Function
    print("Test Case 1 - Basic Function")
    btc = BlockChain()
    btc.add_block("Transaction 1")
    btc.add_block("Transaction 2")
    btc.add_block("Transaction 3")
    btc.add_block("Transaction 4")

    print(btc.to_list())
    print('End of Test Case 1\n')

    # Test Case 2 - Empty Data
    print("Test Case 2 - Empty String Data Field, uncomment\n")
    eth = BlockChain()
    # eth.add_block("")   # we expect a ValueError, invalid data argument

    # Test Case 3 - None Data
    print("Test Case 3 - None Data Field, uncomment\n")
    ada = BlockChain()
    # ada.add_block(None)     # we expect a ValueError, invalid data argument


if __name__ == '__main__':
    main()
