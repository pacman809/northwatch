#!/usr/bin/env python3

from web3 import Web3
import os
import pymongo
import mongo
from datetime import datetime
import search


db 			= "ether1-explorer-mainnet"
myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
mydb 		= myclient[db]
#myCol 		= mydb["temp"]
myCol 		= mydb["temp"]
list 		= []
MN_Array 	= []
percent_base = 0

#--------------------------- MINING REWARDS --------------------------------
try:	
	for x in myCol.find():
		list.extend([x["number"]])
		input = ("wait")
	
	MN_Array 	= mongo.unique(list)
	length 		= len(MN_Array)
	#print("step1")
	#print([x["number"]])


	

	for x in MN_Array:
		#os.system('clear')
		print()
		#print(x)
		percent_base = percent_base + 1
		percent = int(percent_base / length * 100)

		print(f'Percent complete % {percent}')
		print("Mongo")
		mongo.results(x)
		#print(MN_Array)

except TypeError:
	print("No Block Mined.... IF YOU SEE THIS SOMETHING IS REALLY WRONG!!")
	print()
	print()

list 		= []
MN_Array 	= []
myCol.drop()
#------------------------------ GAMES --------------------------------------
