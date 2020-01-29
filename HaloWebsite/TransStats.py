from web3 import Web3
from data import database, timestamp


def TransResults(id):
	
	myCol		=	database()["transactions"]
	
	try:
		for x in myCol.find({"hash" : id}):
			
			x["block_timestamp"] 	= timestamp(x["block_timestamp"])
			x["value"]				= Web3.fromWei(x["value"], 'Ether')

			return x
	except:
		return None
