import pymongo
import datetime
from web3 import Web3
#--------------------CONFIG--------------------------------#

#RPC NODE URL
GethUrl = "http://192.168.1.103:8545"
#

#DATABASE NAME
DataBaseName 	= "halo-explorer-mainnet"
#DataBaseName 	= "halo-explorer-testnet"
#


#---------------------END CONFIG----------------------------#
def database():
	
	db 			= DataBaseName
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb


def timestamp(stamp):
			
			dt 						= datetime.fromtimestamp(stamp // 1000000000)
			s 						= dt.strftime('%Y-%m-%d %H:%M:%S')
			
			return s


def connect_geth():

	web3 = Web3(Web3.HTTPProvider(GethUrl))
	
	return web3

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