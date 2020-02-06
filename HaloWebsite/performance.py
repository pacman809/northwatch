import datetime
from data import database, connect_geth


    
	


def performance():

		
		mydb 		= database()
		myCol 		= mydb["blocks"]

		
		web3 = connect_geth()
		blockNumber2 = web3.eth.blockNumber  #BLOCKNUMBER RESULT
		blockNumber = blockNumber2
		previousBlockNumber = blockNumber - 5
		blockNumber = previousBlockNumber + 1
		averageBlock = blockNumber2 - 1000000

		for x in myCol.find({"number": int(blockNumber)}):
			blockNumber = x["timestamp"]

			for y in myCol.find({"number": previousBlockNumber}):
				previousBlockNumber = y["timestamp"]

				for z in myCol.find({"number": averageBlock}):
					averageBlock = z["timestamp"]
		


		average = blockNumber - averageBlock
		average = average / 1000000
		average = average / 1000000000
		blockTime = blockNumber - previousBlockNumber
		blockTime = blockTime / 1000000000
		times =  datetime.datetime.utcnow() 

		#ROUNDING

		performance={
			"BLOCKNUMBER":	blockNumber2,
			"TIME":			times,
			"BLOCKTIME":	blockTime,
			"AVERAGE":		average
		}

		return performance




