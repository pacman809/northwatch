import pymongo
import json
from datetime import datetime
from web3 import Web3
import requests
#--------------------CONFIG--------------------------------#

#RPC NODE URL
GethUrl = "http://192.168.1.103:8545"
#

#DATABASE NAME
DataBaseName 	= "halo-explorer-mainnet"
#DataBaseName 	= "halo-explorer-testnet"
#


#---------------------END CONFIG----------------------------#
#############################################################
#CONNECTS TO MONGODB # USE CONFIG ABOVE TO ADJUST

def database():
	
	db 			= DataBaseName
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb

#############################################################
#CONVERTS NANOSECOND TIMESTAMP TO REAL TIME LOCAL TO CST

def timestamp(stamp):
			
			dt 						= datetime.fromtimestamp(stamp // 1000000000)
			s 						= dt.strftime('%Y-%m-%d %H:%M:%S')
			
			return s

#############################################################
#CREATES WEB3 INSTANCE TO CONNECT TO 

def connect_geth():

	web3 = Web3(Web3.HTTPProvider(GethUrl))
	
	return web3

#############################################################
#RETURNS BLOCKNUMBER, TIME, BLOCK AVERAGES FOR THE STATS PAGE
def performance():

		
		mydb 		= database()
		myCol 		= mydb["blocks"]

		
		web3 = connect_geth()
		blockNumber2 = web3.eth.blockNumber  #BLOCKNUMBER RESULT
		blockNumber = blockNumber2
		previousBlockNumber = blockNumber - 5
		blockNumber = previousBlockNumber + 1
		averageBlock = blockNumber2 - 1000000

		for x in myCol.find({"number": int(blockNumber)}):
			blockNumber = x["timestamp"]

			for y in myCol.find({"number": previousBlockNumber}):
				previousBlockNumber = y["timestamp"]

				for z in myCol.find({"number": averageBlock}):
					averageBlock = z["timestamp"]
		


		average = blockNumber - averageBlock
		average = average / 1000000
		average = average / 1000000000
		blockTime = blockNumber - previousBlockNumber
		blockTime = blockTime / 1000000000
		times =  datetime.utcnow() 

		#ROUNDING

		performance={
			"BLOCKNUMBER":	blockNumber2,
			"TIME":			times,
			"BLOCKTIME":	blockTime,
			"AVERAGE":		average
		}

		return performance

#############################################################
# SEND IN AN ADDRESS AND IT RETURNS MASTERNODE RESULTS OR A TOTAL OF "NO MASTERNODES"

def masternode(personal_address):
	results = []
	total_shares = float(0)

	api_url = requests.get("https://mn-api.haloplatform.tech/owned/{}".format(personal_address))
	data_results = api_url.json()

	count = len(data_results["result"])

	if count != 0:
		for x in data_results["result"]:
			shares = float('%.08f' % x["SHARES"]) 
			total_shares = shares + total_shares
			shares = Web3.fromWei(shares, 'ETHER')
			totals = Web3.fromWei(total_shares, 'ETHER')

			masternode_shares = {
			"tier" 		:			int(x["TIER"]),
			"shares" 	:		 	int(shares),
			"masternode": 			x["ADDRESS"],
			}

			results.append(masternode_shares)

			tota = {
			"total" 	: totals,
			}
			
			
	

		results.append(tota)
				
		return results

	else:

		total={
		"total" 	: "None"
		}

		results.append(total)
		return results

#############################################################
#RETURNS THE LAST PAYOUT IN HUMAN TIME CST

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
					payout = timestamp(payout)

			return payout

		except:

			payout = "No Data"

			return payout
	

#############################################################
#WHEN THE SEARCH BAR IS ACTIVATED THIS WILL DETERMINE WHETHER ITS AN ADDRESS, BLOCK OR HASH
def query(search):

	search = str(search)
	error = None

	if len(search) == 42:
		search = "https://www.haloexplorer.com/balance/{}".format(search) # is this an address?
		return search

	if len(search) == 66:
		search = "https://www.haloexplorer.com/tx/{}".format(search)#is this a transaction?
		return search

	if len(search) <= 8:
		try:
		   val = int(search)
		   search = "https://www.haloexplorer.com/block/{}".format(search)# is this a block number / invalid at block 100000000 Y2K
		   return search

		except ValueError:
		   return error

##############################################################
#LOADS CONTRACT BALANCES FOR EACH ITEM IN contract_address PULLS BALANCE

def balanceInfo(personal_address):
    results = {}
    contract_address =  ["0xd314d564c36c1b9fbbf6b440122f84da9a551029", "0xc8481effc60fa765ccf8286ba346233ed113b024","0x59195ebd987bde65258547041e1baed5fbd18e8b","0xb8648f065205b9c31055653d668723f4b840e4c0","0x14d01e64f0573925e28d69dc3846b2f0986ab8b8","0x280750ccb7554faec2079e8d8719515d6decdc84","0x0792fe820e7f65da788ac002ce88c74816b59142","0xdc14c317abf4fca7ac2255f0da73b39f63598c76","0x0343350a2b298370381cac03fe3c525c28600b21","0xb70b02222c53abf4e9ccac8fb701425db2ec4de1","0x200941b46e8cbb645fe85cdd526e48826acfd8fa","0x72649f2a739f2ed7454ca146fb9ba589747287f2", "0x1793bc201acbb64f3925ae5cb4355e78864a2597","0xbc77c9ae443940b8ca147870063ee2213264d8b6","0x5f2786097350e9d0a0cbba233774631991dc5e40","0xdfd55110016251c7537d7645f35f92afcfc468ed","0xa6002d6df526683b528f87f95b4903f3c76cb7de","0x9c9b95ed2123c3d7e8e7b65c7cd7b302bc26a13a"]
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
    web3 = connect_geth()
    geth_connect = web3.isConnected()
    account_checksum = Web3.toChecksumAddress(personal_address)
    balance = web3.eth.getBalance(account_checksum)
    halo3 = web3.fromWei(balance, "ether")
    results.update( {"HALO": halo3} )

    for i in contract_address:
        address = Web3.toChecksumAddress(i)
        user_clean = Web3.toChecksumAddress(personal_address)
        contract = web3.eth.contract(address=address, abi=abi)
        symbol = contract.functions.symbol().call()
        balance = contract.functions.balanceOf(user_clean).call()
        balance = web3.fromWei(balance,"ether")

        if symbol == "BTC" and balance != 0 :
            balance = balance * 10000000000
            balance = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
            results.update( {symbol : balance} )
        
        
        if balance != 0:
            results.update( {symbol : balance} )


    return results