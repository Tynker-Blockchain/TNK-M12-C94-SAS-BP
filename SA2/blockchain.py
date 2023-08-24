import hashlib
import json
from time import time
import random

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.miners = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, currentBlock):
        if(len(self.chain) == 0):
            self.createGenesisBlock()  
        currentBlock.previousHash = self.chain[-1].currentHash        
        isBlockMined = currentBlock.mineBlock()
        if(isBlockMined):
            self.chain.append(currentBlock)
            return True
        return False       
    
    def createGenesisBlock(self):
        genesisBlock = Block(0, time(), "No Previous Hash.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transactions", block.transactions)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        previousBlockHash = previousBlock.calculateHash()
        if(previousBlockHash != currentBlock.previousHash):
            return False
        validationHash = currentBlock.calculateHash()
        if(validationHash[0:currentBlock.difficulty] != "0" * currentBlock.difficulty):
            return False
        return True
    
    def addToMiningPool(self, transaction):
        self.pendingTransactions.append(transaction)

    def addMiner(self, miner):
        self.miners.append(miner)

    # Define method minePendingTransactions which takes minerAddress parameter
    
    
        # Loop through each miner in the self.miners
        
           # Check if minerAddress is same as miner.address
            
               # Call miner's createBlock() method and pass length of the chain and pendingTransactions and receive currentBlock
                
                
                # if currentBlock then
                
                    # Validate the block (same code as doe in previous classes in app.py
                    

                        # Remove first three transactions from pendingTransactions
                        
        
class Block:
    def __init__(self, index, timestamp, previousHash):
        self.index = index
        self.transactions = []
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.isValid = None
        self.difficulty = 3
        self.nonce = 0
        self.currentHash = self.calculateHash()
    
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp
        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transactions, default=str) + str(self.nonce)
        return generateHash(blockString)
    
    def mineBlock(self):
        target = "0" * self.difficulty
        nonceLimit = 40000
        
        while self.currentHash[:self.difficulty] != target:
            self.nonce += 1
            self.timestamp = time()    
            self.currentHash = self.calculateHash()        
            
            if(self.nonce >= nonceLimit):
                print("All nonce exhaust")
                self.nonce = 0
        return True

    def addTransaction(self, transaction):
        if transaction:
            self.transactions.append(transaction)
            if len(self.transactions) == 3:
                return "Ready"
            return "Add more transactions"

