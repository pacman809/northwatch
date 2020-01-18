
import pymongo
import datetime
from web3 import Web3
from search import connect_geth



    
	


def performance():

		
		db 			= "halo-explorer-mainnet"
		myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
		mydb 		= myclient[db]
		myCol 		= mydb["blocks"]
		geth_url 	= "http://192.168.1.139:8545"
		list 		= []
		MN_Array 	= []

		
		#print(times)
		web3 = connect_geth()
		blockNumber2 = web3.eth.blockNumber  #BLOCKNUMBER RESULT
		blockNumber = blockNumber2
		previousBlockNumber = blockNumber - 5
		blockNumber = previousBlockNumber + 1
		averageBlock = blockNumber2 - 1000000
		#print(previousBlockNumber)

		for x in myCol.find({"number": int(blockNumber)}):
			blockNumber = x["timestamp"]
			#print(blockNumber)


			for y in myCol.find({"number": previousBlockNumber}):
				previousBlockNumber = y["timestamp"]
				#print(previousBlockNumber)

				for z in myCol.find({"number": averageBlock}):
					averageBlock = z["timestamp"]
		


		average = blockNumber - averageBlock
		average = average / 1000000
		average = average / 100000000000
		blockTime = blockNumber - previousBlockNumber
		blockTime = blockTime / 1000000000
		times =  datetime.datetime.utcnow() 

		#ROUNDING

		

		#print(blockTime)
		performance={
			"BLOCKNUMBER":	blockNumber2,
			"TIME":			times,
			"BLOCKTIME":	blockTime,
			"AVERAGE":		average
		}

		return performance




