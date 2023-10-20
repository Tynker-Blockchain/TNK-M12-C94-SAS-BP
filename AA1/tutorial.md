AA1

Add new Miner
=====================


In this activity, you will learn to add a new miner to the blockchain.

<img src= "https://media.slid.es/uploads/1525749/images/10709135/AA1.gif" width = "480" height = "320">

* Open file app.py


* Create a variable to store the first part of the miner name inside the miningPool() method.


	`minerName = "Miner"`


* Check if the request from the mining pool web page is for mining the pending transactions.
	
    `if "miner" in request.form:`


* Indent the existing code to mine pending transactions under the above if condition. It should look like this:
	
    `if "miner" in request.form:`

    `		minerAddress = request.form.get("miner")`

    `		chain.minePendingTransactions(minerAddress)`


* Else check if the request from the mining pool web page is for adding a new miner.


    `elif "newMiner" in request.form:`


* Increment the total for the second part of the miner name.
	
    `totalMiner += 1`


* Concatenate miner name(first part) with total number of miners(second part).
		
    `minerName = minerName + str(totalMiner)`


* Create the new object of the Miner class.
	
    `newMiner = Miner(minerName)`


* Add the newly created miner to the chain.
		
    `chain.addMiner(newMiner)`


* Save and run the code to check the output.