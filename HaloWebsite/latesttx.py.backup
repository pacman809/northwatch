import inputs
import pymongo

def lastTx():
	
	display = []

	counter = 0
	db 			= "halo-explorer-mainnet"
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]
	myCol 		= mydb["transactions"]
	
	for x in myCol.find({"$and": [ {"to_address": {"$ne": "0x0000000000000000000000000000000000000000"}}]}).limit(100).sort('block_number', pymongo.DESCENDING):
		bob = x["input"]
		bob = str(bob[0:10])

		if bob in inputs.Inputs:
			result = inputs.Inputs[str(bob)](x)
			display.append(result)

	return display

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
