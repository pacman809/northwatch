import pymongo
#from web3 import Web3

def TransResults(id):
	

	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	db 			=	"halo-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"hash" : id}):
			return x
	except:
		return None
"""
TEST

id = "0x690f43fbdd7dc40a1916eb7e2449fd81a701478131a8dc236f3c6b8673cec653"
ANSWER = TransResults(id)
print(ANSWER)
"""

"""
SAMPLE
{
	"_id" : ObjectId("5d06d1b3865f9d31d4b41098"),
	"hash" : "0x690f43fbdd7dc40a1916eb7e2449fd81a701478131a8dc236f3c6b8673cec653",
	"nonce" : 358,
	"block_hash" : "0x9d9fcbdd9fcf82b61fd29b039018d594c274e408c452127dee57fd901b765269",
	"block_number" : 400,
	"transaction_index" : 0,
	"from_address" : "0x6ee7d5471a483d8a72e6f32ecf3d70fdf0a7fe51",
	"to_address" : "",
	"value" : 0,
	"gas" : 90000,
	"gas_price" : 0,
	"input" : "0x686270696e67",
	"block_timestamp" : NumberLong("1527028381468412211")
}
"""