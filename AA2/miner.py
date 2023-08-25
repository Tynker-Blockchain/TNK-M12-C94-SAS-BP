from time import time
from blockchain import Block
from decimal import Decimal


class Miner():
    def __init__(self, address):
        self.address= address
        self.walletBalance = 0    
   
    def createBlock(self, index, transactions):
        if(len(transactions) >=3 ):
            transactions = transactions[:3]

            if index==0:
                index = 1
            blockData = {
                    'index': index,
                    'timestamp': time(),
                    'previousHash': "No Previous Hash.",
            }    

            currentBlock = Block(
                                blockData["index"], 
                                blockData["timestamp"], 
                                blockData["previousHash"])
             
            currentBlock.transactions = transactions
            return currentBlock
        return False
    

    def reward(self, currentBlock, baseReward):
        transactionFee = 0
        for transaction in currentBlock.transactions:
            transactionFee += transaction['transactionFeeEther']

        # Add blockReward and transactionFee to get blockReward 
        
        # Add minerReward to walletBalance
        
