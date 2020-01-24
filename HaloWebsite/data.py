import pymongo


def database():
	db 			= "halo-explorer-mainnet"
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb