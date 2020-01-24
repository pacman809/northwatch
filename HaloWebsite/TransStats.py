import pymongo
from datetime import datetime
from web3 import Web3

def timestamp(stamp):
			
			time 					= stamp
			dt 						= datetime.fromtimestamp(time // 1000000000)
			s 						= dt.strftime('%Y-%m-%d %H:%M:%S')
			
			return s


def TransResults(id):
	

	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	db 			=	"halo-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"hash" : id}):
			
			x["block_timestamp"] 	= timestamp(x["block_timestamp"])
			x["value"]				= Web3.fromWei(x["value"], 'Ether')
			#timestamp = {"block_timestamp": timestamp(x["timestamp"])}
			#x.update(timestamp) 	 
			#x["value"]		= Web3.fromWei(value["value"], "Ether")

			return x
	except:
		return None
