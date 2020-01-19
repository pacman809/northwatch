import pymongo
#from web3 import Web3

def TransResults(id):
	

	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	db 			=	"halo-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"hash" : id}):
			return x
	except:
		return None
