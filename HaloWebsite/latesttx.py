import inputs
import pymongo
from data import database

def lastTx():
	
	display = []

	counter = 0
	
	myCol 		= database()["transactions"]
	
	for x in myCol.find({"$and": [ {"to_address": {"$ne": "0x0000000000000000000000000000000000000000"}}]}).limit(100).sort('block_number', pymongo.DESCENDING):
		bob = x["input"]
		bob = str(bob[0:10])

		if bob in inputs.Inputs:
			result = inputs.Inputs[str(bob)](x)
			display.append(result)

	return display

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
