AA2

Reduce Miner Reward
====================


In this activity, you will add the reward to the miner’s wallet.


* Open the file blockchain.py.


* Create two variables for base reward and reduce reward and initiate them with appropriate values inside the Blockchain class.


    `baseReward = 12.5`

    ` reduceReward = 0`


* Increase the value of reduce reward after every block is mined inside the minePendingTransactions() method.
	
    `BlockChain.reduceReward += 1`


* Decrease the value of base reward after every block is mined.


    `BlockChain.baseReward -= 1/BlockChain.reduceReward`


* Call the reward() method of the miner object with currentBlock to reward the miner.

    `miner.reward(currentBlock, BlockChain.baseReward)`


* Open the file miner.py.


* Remove the code to calculate block reward in reward() method.
	
    `blockReward = Decimal(baseReward) + transactionFee`


* Remove the code to add blockReward to the miner’s wallet balance.
	
    `self.walletBalance += blockReward`


* Save and run the code to check the output.