import pymongo
from web3 import Web3

def blockResults(id):
	

	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	db 			=	"halo-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol 		= 	mydb["blocks"]
	myCol2 		=	mydb["transactions"]
	

	for x in myCol.find({"number" : id}):
		hashy = x["hash"]
		for y in myCol2.find({"block_hash" : hashy }):
			x.update(y)
		return x

test = blockResults(33226666)
print(test)