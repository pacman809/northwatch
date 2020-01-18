import pymongo

def blockResults(id):
	

	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	db 			=	"halo-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol 		= 	mydb["blocks"]
	myCol2 		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"number" : id}):
			hashy = x["hash"]
			for y in myCol2.find({"block_hash" : hashy }):
				x.update(y)
			return x
	except:
		return None
