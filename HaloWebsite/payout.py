#!/usr/bin/env python3


import pymongo 
import time
from datetime import datetime



    
def timestamp(stamp):
		time = 			stamp
		dt = 			datetime.fromtimestamp(time // 1000000000)
		s = 			dt.strftime('%Y-%m-%d %H:%M:%S')
		return s


def payout():

		try:

			db 			= "halo-explorer-mainnet"
			myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
			mydb 		= myclient[db]
			myCol 		= mydb["transactions"]
			list 		= []
			

			for x in myCol.find({"to_address": "0xc660934ec084698e373ac844ce29cf27b104f696"}).limit(1000).sort('block_number', pymongo.DESCENDING):
				
				bob = x["input"]
				bob = str(bob[0:10])

				if bob == "0xdf6c39fb":
					list.append(x["block_timestamp"])
					payout = list[0]
					payout = timestamp(payout)

			return payout

		except:

			payout = "No Data"

			return payout

