#!/usr/bin/env python3

import pymongo
from web3 import Web3
import search
from datetime import datetime


def unique(list1): 
		unique_list = []
		for x in list1:
			if x not in unique_list: 
				unique_list.append(x) 
		for x in unique_list: 
			return unique_list 



def results(address):
	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	#myclient2	=	pymongo.MongoClient("mongodb://halo:halo@45.55.34.86/masternode-api")
	#address2 	= 	Web3.toChecksumAddress(address)
	web3 		= 	search.connect_geth()
	db 			= 	"egem-explorer-mainnet"
	#db2			=   "block_rewards"
	mydb 		= 	myclient[db]
	#mydb2		=	myclient2[db2]
	myCol 		=   mydb["blocks"]
	#myCol 		= 	mydb["temp"]
	myCol2 		= 	mydb["block_rewards"]
	#mycol3		=   mydb2["accountpayout"]
	
	#total 		= 	0
	#list 		= 	[]
	lista 		= 	[]

	#print(myCol)
	#print()
	print(address)
	print()
	for x in myCol.find({"number": address}):
		#print("TEstinG")
		#print(x)
		
	
		try:
			block_number = 	x["number"]
			miner = 		x["miner"]
			miner 	= 	Web3.toChecksumAddress(miner)
			time = 			x["timestamp"]
			dt = 			datetime.fromtimestamp(time)
			s = 			dt.strftime('%Y-%m-%d %H:%M:%S')
			
			#print(s)
			#print(f'Block Number = {block_number}')
			#print(f'Miner = {miner}')
			
			post_reward 	= 	Web3.fromWei(web3.eth.getBalance(miner, block_number),'Ether')
			block_number 	= 	int(block_number)
			block_number 	= 	block_number - 1
			pre_reward 		= 	Web3.fromWei(web3.eth.getBalance(miner, block_number),'Ether')
			reward 			= 	post_reward - pre_reward
			reward1 	= str(reward)
			print(f'Reward = {reward}')
			
			#total = 		total + reward
			
			#print(f'Rewards Total = {total}')
			
			reward = 		str(Web3.toWei(reward,'Ether'))
			
			#print(reward)
			print(miner)
			
			db_entry = {
				"timestamp": x["timestamp"],
				"realtime": s,
				"block_number": x["number"], 
				"hash": x["hash"],
				"owner": x["miner"], 
				"reward": reward1,
				"realreward": reward
				}
			
			
			myCol2.insert_one(db_entry)
			#mycol3.insert_one(db_entry)
			#print()
		except ValueError:
			print("VALUE ERROR MISSING TRIE")
	
	unique(lista)

lista = []
list 		= []
MN_Array 	= []
