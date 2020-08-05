import inputs
import pymongo
from data import database, Onedatabase, Twodatabase

def lastTx(): #HALO
	
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

def OnelastTx(): #ETHER-1
	
	display = []

	counter = 0
	
	myCol 		= Onedatabase()["transactions"]
	myCol2		= Onedatabase()["blocks"]
	
	for x in myCol2.find().limit(100).sort('number', pymongo.DESCENDING):
		
		if x["transaction_count"] != 0:

			#for y in myCol.find().limit(100).sort('block_number', pymongo.DESCENDING):
			for y in myCol.find({"block_number" : x["number"]}):
				bob = y["input"]
				bob = str(bob[0:10])

				if bob in inputs.OneInputs:
					result = inputs.OneInputs[str(bob)](y)
					display.append(result)
		else:

			bob = "blockmined"
			if bob in inputs.OneInputs:
					result = inputs.OneInputs[str(bob)](x)
					display.append(result)
			#result = {
			#"descriptor" : "Block Mined"
			#}
			#display.append(result)

	return display


def TwolastTx(): #EGEM
	
	display = []

	counter = 0
	
	myCol 		= Twodatabase()["transactions"]
	myCol2		= Twodatabase()["blocks"]
	
	for x in myCol2.find().limit(100).sort('number', pymongo.DESCENDING):
		
		if x["transaction_count"] != 0:

			#for y in myCol.find().limit(100).sort('block_number', pymongo.DESCENDING):
			for y in myCol.find({"block_number" : x["number"]}):
				bob = y["input"]
				bob = str(bob[0:10])

				if bob in inputs.TwoInputs:
					result = inputs.TwoInputs[str(bob)](y)
					display.append(result)
		else:

			bob = "blockmined"
			if bob in inputs.TwoInputs:
					result = inputs.TwoInputs[str(bob)](x)
					display.append(result)
			#result = {
			#"descriptor" : "Block Mined"
			#}
			#display.append(result)

	return display
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
