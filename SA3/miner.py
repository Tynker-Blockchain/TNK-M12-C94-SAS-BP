from time import time
from blockchain import Block

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
    
    # Define reward method that takes currentBlock (mined block)
    
        # Formula to calculate the block reward 
        # Block Reward = (Base Reward) + Transaction Fee
        # Set initial value of baseReward to 5 i.e base value
        
        # Set transaction fee to 0
        
        # Lop through each transaction in transactions
        
            # Add transaction['transactionFeeEther'] to transactionFee
            

        # Add blockReward and transactionFee to get blockReward 
        
        # Add minerReward to walletBalance
   