
# Dictionary of Inputs
# Top SECRET *** I will find you :)
from web3 import Web3
#import json
#import simplejson as json
from datetime import datetime
#from inputFunction import parse
#from inputFunction import hextodec
#from inputFunction import dectohex
#from contracts import contractType

Inputs	= {
	
	"0x": 			"interHalo", #Done
	"0x0029185b": 	"noInfo",	
	"0x00e77545": 	"bcwithdrawl",	
	"0x0309bebc": 	"noInfo",	
	"0x03e985d9": 	"noInfo",	
	"0x04e27777": 	"noInfo",	
	"0x06862706": 	"noInfo",	
	"0x095ea7b3": 	"ethTransferWallettoDex1",
	"0x338b5dea":   "ethTransferWallettoDex2",
	"0x0b927666": 	"dexPlaceOrder",
	"0x0c8e8326": 	"noInfo",
	"0x13a30791": 	"noInfo",
	"0x19f7ae27": 	"noInfo",
	"0x2a95599f": 	"MarketplaceCancelOrder",
	"0x2e1a7d4d": 	"haloFromDexToWallet",
	"0x31663639": 	"dexFilledOrder",
	"0x44811585": 	"serviceFee",
	"0x4b67e07f": 	"noInfo",
	"0x4d4ea199": 	"noInfo",
	"0x4e656f5f": 	"noInfo",
	"0x5848e444": 	"noInfo",
	"0x5bd05f7f": 	"noInfo",
	"0x60606040": 	"contractDeployment",
	"0x61443a5f": 	"noInfo",
	"0x65863672": 	"noInfo",
	"0x68627069": 	"noInfo",
	"0x6d69fcaf": 	"noInfo",
	"0x6f0ef949": 	"noInfo",
	"0x726c4d6f": 	"CommitToSharedContract",
	"0x749726fe": 	"noInfo",
	"0x76319190": 	"noInfo",
	"0x763819ea": 	"masternodeCreate",
	"0x792fa508": 	"masternodeSuspend",
	"0x7c325d0e": 	"masternodeTerminate",
	"0x7f746573": 	"noInfo",
	"0x8255069d": 	"dexOrderCancelled",
	"0x9407ea98": 	"noInfo",
	"0x976640e2": 	"noInfo",
	"0x98ca05eb": 	"noInfo",
	"0x99404220": 	"noInfo",
	"0x9e281a98": 	"hethToEth",
	"0x9f8a89ba": 	"nodeActivate",
	"0xa9059cbb": 	"WrappedTokenTransfer",
	"0xb214faa5": 	"gamesDeposit",
	"0xb36c2acc": 	"ethOffNetwork",
	"0xb5ec9999": 	"noInfo",
	"0xc885bc58": 	"masternodePayout",
	"0xc94ee098": 	"noInfo",
	"0xcbb0f029": 	"boughtMarketplace",
	"0xceeb7066": 	"noInfo",
	"0xd0e30db0": 	"HaloWalletToDex",
	"0xd4444da6": 	"masternodeSell",
	"0xdf6c39fb": 	"payout",
	"0xea115fdb": 	"noInfo",
	"0xf612f5ce": 	"noInfo",
	"0xff3252a1": 	"noInfo",
	"0x68627069":   "systemPing",
	"0xd28c25d4":	"Smart Contract"
}

def HexToDec(hex):
	
	x = 	int(hex, 16)
	x = 	str(x)
	
	return 	x



def DecToHex(dec):
	x = 	int(dec)
	x =		hex(x)

	return x



def InputParse(input):
	
	fields =  		int(len(input))
	fieldlenth = 	fields - 10
	fieldNumber = 	fieldlenth/64
	a = 			10 
	x = 			1
	list = 			[input[0:10]]

	while x <= fieldNumber:
		b = 		a + 64
		sector = 	input[a:b]
		sect = 		HexToDec(sector)
		#print(sect)
		a = 		b
		x = 		x + 1
		list.append(sect)
	return list	

#input = "0x0b927666000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010f0cf064dd59200000000000000000000000000000d314d564c36c1b9fbbf6b440122f84da9a55102900000000000000000000000000000000000000000000000000096a2934a7a000000000000000000000000000000000000000000000000000000000003db4bdb700000000000000000000000000000000000000000000000000000000000000ca"
#

def GetType(inpoot):
	answer = InputParse(inpoot)
	if answer[0] in Inputs :
		type = answer[0]
		#print("documented")
		type = Inputs[type]
	#print(type)
	#print(answer)
		answer = [type] + answer
	#answer.append(type)
	#fields = len(answer)
	#print(answer)
		return(answer)
	else:
		answer = "0x00000000"
		type = "Unknown"
		answer = type + answer
		return answer

	#print(fields)
	#print(int(answer[2]))
	#count = 0

#test = GetType("0x0b927666000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010f0cf064dd59200000000000000000000000000000d314d564c36c1b9fbbf6b440122f84da9a55102900000000000000000000000000000000000000000000000000096a2934a7a000000000000000000000000000000000000000000000000000000000003db4bdb700000000000000000000000000000000000000000000000000000000000000ca")
#print(test)
#rint(f'Input 				{answer[0]} Filled Dex Order')
#print(f'Contract Address 		DEX {DecToHex(answer[1])}')
#print(f'Token Contract Base Pair 	ETH {DecToHex(answer[2])}')
#value = int(answer[3])
#value = Web3.fromWei(value, 'Ether')
#print(f'Total Base Pair 		{value}')
#value = int(answer[3])
#value = Web3.fromWei(value, 'Ether')
#print(f'Shares for Sale 		{value}')
#value = int(answer[4])
#value = Web3.fromWei(value, 'Ether')
#print(f'Asking Price 		{value}')
#print(f'Order Number?			{answer[7]}')
#print(f'Address? = 			{DecToHex(answer[8])}')
#print(answer[9])
#print(answer[10])
#print(answer[11])
#value = int(answer[12])
#value = Web3.fromWei(value, 'Ether')
#print(answer[12])
#print(f' 				{value}')
#print(answer[13])



#------------------------------------------------------------------------------------------------------------
#GENERAL TRANSACTION






def timestamp(stamp):
			time = 			stamp
			dt = 			datetime.fromtimestamp(time // 1000000000)
			s = 			dt.strftime('%Y-%m-%d %H:%M:%S')
			return s



def interHalo(receivedInput):
	
	DESCRIPTOR = "Interhalo Transaction"
	
	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	}
	

	y = json.dumps((result),sort_keys=True, indent=4, separators=(',', ': '))
	#print(DESCRIPTOR)
	#print("P2P Transaction")
	print(result)
	#return result
	#COMPLETED

#NOINFO DEFAULT

def noInfo(receivedInput):

	DESCRIPTOR = "PLEASE REPORT BLOCK NUMBER AND A BREIF SUMMARY OF WHAT YOU THINK THIS IS"
	

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	}
	

	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)
	#COMPLETED
#------------------------------------------------------------------------------------------------------------
#MASTERNODES

def masternodePayout(receivedInput):

	DESCRIPTOR = "Masternode Payout"

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	}
	

	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)


def masternodeSell(receivedInput): #0xd4444da6
	
	DESCRIPTOR = "Masternode Sell Order on Marketplace"
	data = receivedInput["input"]

	answer = parse(data)
	masternode = dectohex(answer[0])
	

	shares_for_sale = int(answer[2])
	shares_for_sale = Web3.fromWei(shares_for_sale, 'Ether')
	asking_price = int(answer[3])
	asking_price = Web3.fromWei(asking_price, 'Ether')


	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	#"seller"				: receivedInput["from_address"],
	#"shares_for_sale"		: str(shares_for_sale),
	#"asking_price"			: str(asking_price),
	#"masternode"			: masternode
	"input"					: {"masternode": masternode, "shares_for_sale": str(shares_for_sale), "asking_price": str(asking_price), "seller": receivedInput["from_address"]}
	}
	

	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)

	#COMPLETED

def masternodeCreate(receivedInput):
	DESCRIPTOR = "MASTERNODE Creation"

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	#"ip_address"			: "IP ADDRESS HERE / DETERMINES LOCATION. AND SELF HOSTED OR NOT"
	}
	
	print(receivedInput["value"])
	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)


def masternodeTerminate(receivedInput):
	DESCRIPTOR = "MASTERNODE Terminated"

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	}
	

	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)


#------------------------------------------------------------------------------------------------------------
#DEX

def dexPlaceOrder(receivedInput):
	DESCRIPTOR = "Dex Trade Order"

	data = receivedInput["input"]
	answer = parse(data)
	orderNumber = str(answer[4])
	Wanting =  dectohex(answer[0])
	Wanting = contractType(Wanting)
	shares_wanted = int(answer[1])
	shares_wanted2 = str(Web3.fromWei(shares_wanted, 'Ether'))
	giveCoin = int(answer[3])
	giveCoin2 = str(Web3.fromWei(giveCoin, 'Ether'))
	Giving = contractType(answer[2])
	#price =float(shares_wanted2) / float(giveCoin2)

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"inputs" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"input"					: {"orderNumber": answer[4], "amountWanted": shares_wanted2, "wantCoin": Wanting,  "amountGiving": giveCoin2, "giveCoin": Giving }
	}

	

	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)


def dexFilledOrder(receivedInput):
	print("Dex Filled/Completed Order")


def dexOrderCancelled(receivedInput):
	print("Dex Order Cancelled")	


#------------------------------------------------------------------------------------------------------------
#ETH

def ethTransferWallettoDex1(receivedInput):
	DESCRIPTOR = ("ETH Transfer from Wallet to Dex 1st TX (Sent From Halo Wallet to Dex)")

	#inputParse(receivedInput)
	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	}


	def dexPlaceOrder(receivedInput):
		DESCRIPTOR = "Dex Sell Order placed for sale"


		
		

		y = json.dumps(result)
	#	print(DESCRIPTOR)
		print(result)
	


def ethTransferWallettoDex2(receivedInput):
	print("ETH Transfer from wallet to Dex 2nd Tx (Sent to DEX side Wallet)")	


def hethToEth(receivedInput):
	print("ETH Convert HETH to ETH")


def ethOffNetwork(receivedInput):
	print("ETH Sent off Halo to Eth address")

#----------------------------------------------------------------------------------------------------------
#GAMES

def gamesDeposit(receivedInput):
	
	DESCRIPTOR = "Block and Chain Game Deposit"

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	#"input" 				: receivedInput['input'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	}
	

	y = json.dumps(result)
	#print(DESCRIPTOR)
	print(result)








