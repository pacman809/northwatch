import pymongo
import inputs
from web3 import Web3
from data import database, Onedatabase, connect_geth, one_connect_geth

def getAccountHistory(user_address):

	display					= []
	transactionCount 		= []

	myCol 					= database()["transactions"]

	user_address_Checksum 	= Web3.toChecksumAddress(user_address)
	transactionCount 		= connect_geth().eth.getTransactionCount(user_address_Checksum)
	userEntry 				= normalized_address = '0x{}'.format(user_address[2:].lstrip('0'))
	userEntry 				= user_address.lower()


	for x in myCol.find( { "$or": [ { "from_address": userEntry }, { "to_address": userEntry } ] } ).limit(400).sort('block_number', pymongo.DESCENDING):
		bob = x["input"]
		bob = str(bob[0:10])

		if bob in inputs.Inputs:
			result = inputs.Inputs[str(bob)](x)

			if result["to_address"] == userEntry:
				result["direction"] = "in"
				display.append(result)
			else:
				result["direction"] = "out"
				display.append(result)	

	count = transactionCount
	return display ,count


def OnegetAccountHistory(user_address):

	display					= []
	transactionCount 		= []

	myCol 					= Onedatabase()["transactions"]

	user_address_Checksum 	= Web3.toChecksumAddress(user_address)
	transactionCount 		= one_connect_geth().eth.getTransactionCount(user_address_Checksum)
	userEntry 				= normalized_address = '0x{}'.format(user_address[2:].lstrip('0'))
	userEntry 				= user_address.lower()


	for x in myCol.find( { "$or": [ { "from_address": userEntry }, { "to_address": userEntry } ] } ).limit(400).sort('block_number', pymongo.DESCENDING):
		bob = x["input"]
		bob = str(bob[0:10])

		if bob in inputs.OneInputs:
			result = inputs.OneInputs[str(bob)](x)

			if result["to_address"] == userEntry:
				result["direction"] = "in"
				display.append(result)
			else:
				result["direction"] = "out"
				display.append(result)	

	count = transactionCount
	return display ,count
