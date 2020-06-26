#!/usr/bin/env python3

import pymongo
import time
from web3 import Web3




display = []
documented = []

counter = 0
db 			= "halo-explorer-mainnet"
myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
mydb 		= myclient[db]
myCol3		= mydb["temp"]
myCol 		= mydb["transactions"]
mycol2		= mydb["ethereum"]
base = 100000000
iter = 0



def hextodec(hex):					#Converts Decimal To Hex
	
	x = 	int(hex, 16)
	x = 	str(x)
	
	return 	x


def dectohex(dec):
	x = 	int(dec)
	x =		hex(x)

	return x


def parse(input):				#Takes Input And Parses 
	
	fields =  		int(len(input))
	fieldlenth = 	fields - 10
	fieldNumber = 	fieldlenth/64
	a = 			10 
	x = 			1
	list = 			[]

	while x <= fieldNumber:
		b = 		a + 64
		sector = 	input[a:b]
		sect = 		hextodec(sector)
		a = 		b
		x = 		x + 1
		list.append(sect)
	
	return list	




for x in mycol2.find():
		documented.extend([x["block_timestamp"]])

		

for x in myCol3.find( { "to_address" : "0xd314d564c36c1b9fbbf6b440122f84da9a551029" } ):
		if x['block_timestamp'] in documented:
			print("Already DataBased")
			continue
		try:
			bob = x["input"]
			bob = str(bob[0:10])
			if bob == "0xea115fdb":
			
				print("New Entry")


				parsed = parse(x["input"])
				address = dectohex(parsed[0])
				value = parsed[1]
				#value = Web3.fromWei(value , 'ETHER' )
				
				entry ={
			
			"hash" : x["hash"],
			"nonce" : x["nonce"],
			"block_hash" : x["block_hash"],
			"block_number" : x["block_number"],
			"transaction_index" : x["transaction_index"],
			"from_address" : x["from_address"],
			"to_address" : address,
			"value" : value,
			"gas" : x["gas"],
			"gas_price" : x["gas_price"],
			"input" : x["input"],
			"block_timestamp" : x["block_timestamp"]
			}

				mycol2.insert_one(entry)
				print(entry)

		except ValueError:
			print("VALUE ERROR MISSING TRIE")

myCol3.drop()
