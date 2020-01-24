#!/usr/bin/env python3

from web3 import Web3
import os
import pymongo
import mongo
from datetime import datetime
import search


db 			= "halo-explorer-mainnet"
myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
mydb 		= myclient[db]
#myCol 		= mydb["temp"]
myCol 		= mydb["temp"]
list 		= []
MN_Array 	= []
percent_base = 0

#--------------------------- MASTERNODES --------------------------------
try:	
	for x in myCol.find({"input": "0xc885bc58"}):
		list.extend([x["from_address"]])
		input = ("wait")
	
	MN_Array 	= mongo.unique(list)
	length 		= len(MN_Array)
	print("step1")
	print([x["from_address"]])


	

	for x in MN_Array:
		#os.system('clear')
		print()
		print(x)
		percent_base = percent_base + 1
		percent = int(percent_base / length * 100)
		print(f'Percent complete % {percent}')
		print("Mongo")
		mongo.results(x)
		print(MN_Array)

except TypeError:
	print("No New Masternode Withdrawls!")
	print()
	print()

list 		= []
MN_Array 	= []
#------------------------------- GAMES --------------------------------------
