#!/usr/bin/env python3


import pymongo 
from data import timestamp, database



    

def payout():

		try:

			myCol 		= database()["transactions"]
			list 		= []
			

			for x in myCol.find({"to_address": "0xc660934ec084698e373ac844ce29cf27b104f696"}).limit(1000).sort('block_number', pymongo.DESCENDING):
				
				bob = x["input"]
				bob = str(bob[0:10])

				if bob == "0xdf6c39fb":
					list.append(x["block_timestamp"])
					payout = list[0]
					payout = data.timestamp(payout)

			return payout

		except:

			payout = "No Data"

			return payout

