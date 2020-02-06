import pymongo
from datetime import datetime
from web3 import Web3
#--------------------CONFIG--------------------------------#

#RPC NODE URL
GethUrl = "http://192.168.1.103:8545"
#

#DATABASE NAME
DataBaseName 	= "halo-explorer-mainnet"
#DataBaseName 	= "halo-explorer-testnet"
#


#---------------------END CONFIG----------------------------#
def database():
	
	db 			= DataBaseName
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb


def timestamp(stamp):
			
			dt 						= datetime.fromtimestamp(stamp // 1000000000)
			s 						= dt.strftime('%Y-%m-%d %H:%M:%S')
			
			return s


def connect_geth():

	web3 = Web3(Web3.HTTPProvider(GethUrl))
	
	return web3