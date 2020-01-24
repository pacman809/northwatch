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
	myclient2	=	pymongo.MongoClient("mongodb://halo:halo@45.55.34.86/masternode-api")
	address2 	= 	Web3.toChecksumAddress(address)
	web3 		= 	search.connect_geth()
	db 			= 	"halo-explorer-mainnet"
	db2			=   "masternode-api"
	mydb 		= 	myclient[db]
	mydb2		=	myclient2[db2]
	myCol 		= 	mydb["transactions"]
	mycol2 		= 	mydb["masternodes"]
	mycol3		=   mydb2["accountpayout"]
	
	total 		= 	0
	list 		= 	[]
	lista 		= 	[]

	for x in mycol2.find({"from_address": address}):
		list.extend([x["timestamp"]])
		lista.extend([x["masternode"]])
	
	for x in myCol.find({"from_address": address, "input": '0xc885bc58'}):
		if x['block_timestamp'] in list:
			print("Already DataBased")
			continue
		try:
			block_number = 	x["block_number"]
			masternode = 	x["to_address"]
			time = 			x["block_timestamp"]
			dt = 			datetime.fromtimestamp(time // 1000000000)
			s = 			dt.strftime('%Y-%m-%d %H:%M:%S')
			
			print(s)
			print(f'Block Number = {block_number}')
			print(f'Masternode = {masternode}')
			
			post_reward 	= 	Web3.fromWei(web3.eth.getBalance(address2, block_number),'Ether')
			block_number 	= 	int(block_number)
			block_number 	= 	block_number - 1
			pre_reward 		= 	Web3.fromWei(web3.eth.getBalance(address2, block_number),'Ether')
			reward 			= 	post_reward - pre_reward
			reward1 	= str(reward)
			print(f'Reward = {reward}')
			
			total = 		total + reward
			
			print(f'Rewards Total = {total}')
			
			reward = 		str(Web3.toWei(reward,'Ether'))
			
			print()
			
			db_entry = {
				"timestamp": x["block_timestamp"],
				"realtime": s,
				"block_number": x["block_number"], 
				"hash": x["hash"],
				"owner": x["from_address"], 
				"masternode": x["to_address"],
				"reward": reward1,
				"realreward": reward
				}
			
			
			mycol2.insert_one(db_entry)
			#mycol3.insert_one(db_entry)
			#print()
		except ValueError:
			print("VALUE ERROR MISSING TRIE")
	
	unique(lista)

lista = []
list 		= []
MN_Array 	= []
