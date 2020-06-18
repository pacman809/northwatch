import pymongo
from web3 import Web3
from data import connect_geth, timestamp, database, onetimestamp, one_connect_geth, Onedatabase

#------------------------------------------------------------------------------------------------------------
#GENERAL TRANSACTION
def hextodec(hex):					#Converts Decimal To Hex
	
	x = 	int(hex, 16)
	x = 	str(x)
	
	return 	x


def dectohex(dec):
	x = 	int(dec)
	x =		hex(x)

	return x


def parse(input):				#Takes Input And Parses 
	
	fields 		=	int(len(input))
	fieldlenth 	= 	fields - 10
	fieldNumber = 	fieldlenth/64
	a 			= 	10 
	x 			= 	1
	list		= 	[]

	while x <= fieldNumber:
		b 		= 	a + 64
		sector 	= 	input[a:b]
		sect 	= 	hextodec(sector)
		a 		= 	b
		x 		= 	x + 1

		list.append(sect)
	
	return list	

#-----------------------------------------------------------------------------------------------------------

known_address_contract={

	"0x45842a0f603ef5a5aa44503767c6ab9fd03d824e"	: "STEX Hot Wallet",
	"0x630583fde8e6899c74d942814a3719b6d544220e"	: "Northwatch Donations",
	"0xc8a9d002fdaebf5bf03d530c3047d96b44257f10"	: "T4i MN Pool",
	"0x3fcf16e7090fe013b5648d796908916b2290b6c6"	: "Block And Chain Games",
	"0x5271aa0ec2e9cc54db55136554a10cf2f7daa82b"	: "HaloDex SC",
	"0x123ea742a564eaa8e83871618bd9baaf400ff482"	: "LAToken Hot Wallet"

	}

#-----------------------------------------------------------------------------------------------------------


def tokenType(contract):

	tokens={
	"0x0"	: "HALO",
	"0xd314d564c36c1b9fbbf6b440122f84da9a551029"	: "ETH",
	"0xc8481effc60fa765ccf8286ba346233ed113b024"	: "BAT",
	"0x59195ebd987bde65258547041e1baed5fbd18e8b"	: "DBET",
	"0xb8648f065205b9c31055653d668723f4b840e4c0"	: "BTC", #8 Decimals
	"0x14d01e64f0573925e28d69dc3846b2f0986ab8b8"	: "HST",
	"0x280750ccb7554faec2079e8d8719515d6decdc84"	: "VET",
	"0x0792fe820e7f65da788ac002ce88c74816b59142"	: "OMG",
	"0xdc14c317abf4fca7ac2255f0da73b39f63598c76"	: "USDC",
	"0x343350a2b298370381cac03fe3c525c28600b21"		: "VTHO",
	"0xb70b02222c53abf4e9ccac8fb701425db2ec4de1"	: "ZRX",
	"0x200941b46e8cbb645fe85cdd526e48826acfd8fa"	: "FLASH",
	"0x72649f2a739f2ed7454ca146fb9ba589747287f2"	: "UDOO",
	"0x792fe820e7f65da788ac002ce88c74816b59142"		: "VTHO",
	"0xc57b9e7a29bc7fa4ee9e23994105a3c0278832cd"	: "TOKEN",
	"0x7cb51f76837e4c0e48cdabdf01107ca90bdbe561"    : "TOKEN2",
	"0x32e31f27aaf3501a4f7139970477020baf9c8e1c"	: "TESTP", #PEG
	"0x9c9b95ed2123c3d7e8e7b65c7cd7b302bc26a13a"	: "TEST", #???
	"0xdf5e6ded3dfe4041519eb9d1e57dbe71b2760262"	: "F1", #FCT
	"0xc43a6a22d3a430f175a994683005572cdb18f47c"	: "TEST", #Halo Classic Test
	"0x1793bc201acbb64f3925ae5cb4355e78864a2597"	: "HALOC", #Halo Classic Legit
	"0x5f2786097350e9d0a0cbba233774631991dc5e40"	: "EVED", #EVED
	"0x0023bc712073f013fd810693a7c40da5002e9b84"	: "Dud", #TUTOTEST
	"0xbc77c9ae443940b8ca147870063ee2213264d8b6"	: "WIZARD", #WIZARD
	"0xf6ad1612a655977ed1d0934aefa541f8660ee3a2"	:"UNKNOWN",
	"0xddb500dbe30c91398a2ade12234d4075aabea650"	: "XXX"	, #FACTOM
	"0x978dc9ca2d75c9d187a9cb542c74c50c579a034a"	: "F2",
	"0xdfd55110016251c7537d7645f35f92afcfc468ed" 	: "HXRO", #
	"0xa6002d6df526683b528f87f95b4903f3c76cb7de"	: "FCT", #8 decimals
	"0x4734e87fbd52516ff729345bbf910557f630477c"	: "PEGNET",
	"0x0343350a2b298370381cac03fe3c525c28600b21"	: "VTHO"

	}

	Onetokens		={
	"0xf69bc54fda5d2689a4d4fe8c1e6a5cbc25f6dc59",	#VOTE
	"0x92e6c6eee2d4de4585ffe101e1e3288fb4e28330",	#KOT
	"0xa888fbc3f9ca63776913d807804fc31c5ebda6d7",	#KOT
	"0xc715e66000ceaee350c82c34b9b153c3c52f295b"	#BTC

	}

	x = str(contract)
	coin = tokens[x]
	return coin

#-----------------------------------------------------------------------------------------------------------


def hotlist(hotlist):


	if hotlist in known_address_contract:
			x = str(hotlist)
			known = known_address_contract[x]
			return known
	else :
			return hotlist

#-----------------------------------------------------------------------------------------------------------


def MNPAYOUT(to_address):

	address 						= Web3.toChecksumAddress(to_address)
	web3 							= connect_geth()
	mydb 							= database()
	myBlock 						= mydb["blocks"]
	myCol 							= mydb["transactions"]
	
	
	
	for x in myCol.find({"to_address": to_address, "input": '0xc885bc58'}):

		block_number 				= x["block_number"]
		post_reward 				= Web3.fromWei(web3.eth.getBalance(address, block_number),'Ether')
		block_number 				= int(block_number)
		block_number 				= block_number - 1
		pre_reward 					= Web3.fromWei(web3.eth.getBalance(address, block_number),'Ether')
		reward 						= pre_reward - post_reward
		result						= reward
	

		return result


#-----------------------------------------------------------------------------------------------------------


def systemPing(receivedInput):

	DESCRIPTOR = "System Ping"

	value                           = Web3.fromWei(receivedInput['value'], 'Ether')
	description                     = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	
	result							= {

	"descriptor"                    : DESCRIPTOR,
	"hash"                          : receivedInput['hash'],
	"nonce"                         : receivedInput['nonce'],
	"block_hash"                    : receivedInput['block_hash'],
	"block_number"                  : receivedInput['block_number'],
	"transaction_index"             : receivedInput['transaction_index'],
	"from_address"                  : receivedInput['from_address'],
	"to_address"                    : receivedInput['to_address'],
	"value"                         : value,
	"gas"                           : receivedInput['gas'],
	"gas_price"                     : receivedInput['gas_price'],
	"block_timestamp"               : timestamp(receivedInput['block_timestamp']),
	"description"					: description
						
	}


	return result




#----------------INPUTS-------HERE-----------------------------------------------------------------



def interHalo(receivedInput):
	
	DESCRIPTOR = "Interhalo Transaction"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result
	

def etherOneTx(receivedInput):
	
	DESCRIPTOR = "Ether-1 Transaction"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result	

def bot_tip(receivedInput):
	
	DESCRIPTOR = "Tip Bot"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result		
#---------------------------------------------------------------------------------------------------

def Burn(receivedInput):
	
	DESCRIPTOR = "Token Burned"

	result = parse(receivedInput["input"])
	value					= Web3.fromWei(int(result[0]), 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	



	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result
	
#---------------------------------------------------------------------------------------------------

def ContractDeploy(receivedInput):
	
	DESCRIPTOR = "CONTRACT DEPLOY"
	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
	
#---------------------------------------------------------------------------------------------------


def SmartContract(receivedInput):
	
	DESCRIPTOR = "Smart Contract Interaction"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result
	
#---------------------------------------------------------------------------------------------------

def payout(receivedInput):
	
	DESCRIPTOR = "MN Payout"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result
	
#---------------------------------------------------------------------------------------------------
def CommitToSharedContract(receivedInput): #"0x726c4d6f": 	,
	
	DESCRIPTOR = "Commit To MN Contract"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#-----------------------------------------------------------------------------------------------------------

def noInfo(receivedInput):

	DESCRIPTOR = "PLEASE REPORT BLOCK NUMBER AND A BREIF SUMMARY OF WHAT YOU THINK THIS IS"
	description = f'Unknown At the Current Time'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
#------------------------------------------------------------------------------------------------------------


def ERCDeposit(receivedInput):

	DESCRIPTOR = "ERC20 Deposited"
	description = "nil"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
#------------------------------------------------------------------------------------------------------------
#MASTERNODES



def DepositEth(receivedInput):

	mydb 		= 	database()
	myETH		= 	mydb["ethereum"]


	DESCRIPTOR = "Ether Deposited"
	timestampCheck   = receivedInput["block_timestamp"]

	try:
		for x in myETH.find({ "block_timestamp" : timestampCheck }):
			x['value'] = int(x['value'])
			#value			= Web3.fromWei(x['value'], 'Ether')
			value 					= x['value'] / 1000000000000000000
			value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
			description 	= f'Databased ETH Deposit'
		
			result={
			"descriptor"			: DESCRIPTOR,
			"hash" 					: x['hash'],			
			"nonce"					: x['nonce'],
			"block_hash"			: x['block_hash'],
			"block_number"			: x['block_number'],
			"transaction_index"		: x['transaction_index'],
			"from_address"			: x['from_address'],
			"to_address"			: x['to_address'],
			"value"					: value,
			"gas" 					: x['gas'],
			"gas_price"				: x['gas_price'],
			"block_timestamp"		: timestamp(x['block_timestamp']),
			"description"			: description
			}
			

			y = result
			
			return y

	except:
			receivedInput['value'] = int(x['value'])
			#value			= Web3.fromWei(x['value'], 'Ether')
			value 					= x['value'] / 1000000000000000000
			value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
			description 	= f'Calculated ETH Deposit'
		
			result={
			"descriptor"			: DESCRIPTOR,
			"hash" 					: receivedInput['hash'],			
			"nonce"					: receivedInput['nonce'],
			"block_hash"			: receivedInput['block_hash'],
			"block_number"			: receivedInput['block_number'],
			"transaction_index"		: receivedInput['transaction_index'],
			"from_address"			: receivedInput['from_address'],
			"to_address"			: receivedInput['to_address'],
			"value"					: value,
			"gas" 					: receivedInput['gas'],
			"gas_price"				: receivedInput['gas_price'],
			"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
			"description"			: description
			}
				

			y = result
				
			return y

	
#------------------------------------------------------------------------------------------------------------

def masternodePayout(receivedInput):

	mydb 		= 	database()
	myMN		= 	mydb["masternodes"]

	DESCRIPTOR = "Claimed MN Reward"
	to_address = receivedInput["to_address"]
	checkHash  = receivedInput["block_timestamp"]

	try:
		for x in myMN.find({ "timestamp" : checkHash }):
			reward = x["reward"]

			description = f'Masternode {receivedInput["to_address"]} Payout'
		
		result={
		"descriptor"			: DESCRIPTOR,
		"hash" 					: receivedInput['hash'],			
		"nonce"					: receivedInput['nonce'],
		"block_hash"			: receivedInput['block_hash'],
		"block_number"			: receivedInput['block_number'],
		"transaction_index"		: receivedInput['transaction_index'],
		"from_address"			: receivedInput['from_address'],
		"to_address"			: receivedInput['to_address'],
		"value"					: reward,
		"gas" 					: receivedInput['gas'],
		"gas_price"				: receivedInput['gas_price'],
		"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
		"description"			: description,
		"reward"				: reward
		}
		

		y = result
		
		return y

	except:
		reward = MNPAYOUT(to_address)

		description = f'Masternode {receivedInput["to_address"]} Payout'
		
		result={
		"descriptor"			: DESCRIPTOR,
		"hash" 					: receivedInput['hash'],			
		"nonce"					: receivedInput['nonce'],
		"block_hash"			: receivedInput['block_hash'],
		"block_number"			: receivedInput['block_number'],
		"transaction_index"		: receivedInput['transaction_index'],
		"from_address"			: receivedInput['from_address'],
		"to_address"			: receivedInput['to_address'],
		"value"					: reward,
		"gas" 					: receivedInput['gas'],
		"gas_price"				: receivedInput['gas_price'],
		"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
		"description"			: description,
		"reward"				: reward
		}
		

		y = result
		return y

#---------------------------------------------------------------------------------------------------------------

def HaloWalletToDex(receivedInput): #0xd0e30db0

	DESCRIPTOR = "Wallet --> HaloDex"
	#value                                   = Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	#to_address_known = hotlist(receivedInput["to_address"])
	#from_address_known = hotlist(receivedInput["from_address"])

	result={
	"descriptor"                    : DESCRIPTOR,
	"hash"                          : receivedInput['hash'],
	"nonce"                         : receivedInput['nonce'],
	"block_hash"                    : receivedInput['block_hash'],
	"block_number"                  : receivedInput['block_number'],
	"transaction_index"             : receivedInput['transaction_index'],
	"from_address"                  : receivedInput['from_address'],
	"to_address"                    : receivedInput['to_address'],
	"value"                         : value,
	"gas"                           : receivedInput['gas'],
	"gas_price"                     : receivedInput['gas_price'],
	"block_timestamp"               : timestamp(receivedInput['block_timestamp']),
	"description"                   : description
	}

	return result


#---------------------------------------------------------------------------------------------------------------



	
def haloFromDexToWallet(receivedInput): #"0x2e1a7d4d"

	DESCRIPTOR = "HaloDex --> Wallet"

	scrape = parse(receivedInput["input"])
	scrape = int(scrape[0])
	#value      = str(Web3.fromWei(scrape, 'Ether'))
	value 					= scrape / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result={
	"descriptor"                    : DESCRIPTOR,
	"hash"                          : receivedInput['hash'],
	"nonce"                         : receivedInput['nonce'],
	"block_hash"                    : receivedInput['block_hash'],
	"block_number"                  : receivedInput['block_number'],
	"transaction_index"             : receivedInput['transaction_index'],
	"from_address"                  : receivedInput['from_address'],
	"to_address"                    : receivedInput['to_address'],
	"value"                         : value,
	"gas"                           : receivedInput['gas'],
	"gas_price"                     : receivedInput['gas_price'],
	"block_timestamp"               : timestamp(receivedInput['block_timestamp']),
	"description"                   : description
	}

	return result


#----------------------------------------------------------------------------------------------------------


def masternodeSell(receivedInput): #0xd4444da6
	
	DESCRIPTOR = "Masternode Sell Order on Marketplace"
	data = receivedInput["input"]

	answer = parse(data)
	masternode = dectohex(answer[0])
	

	shares_for_sale = int(answer[2])
	shares_for_sale = Web3.fromWei(shares_for_sale, 'Ether')
	asking_price = int(answer[3])
	asking_price = Web3.fromWei(asking_price, 'Ether')
	ratio = "{:.2f}".format(shares_for_sale/asking_price)
	
	result={
    "descriptor"                    : DESCRIPTOR,
    "hash"                          : receivedInput['hash'],
    "nonce"                         : receivedInput['nonce'],
    "block_hash"                    : receivedInput['block_hash'],
    "block_number"                  : receivedInput['block_number'],
    "transaction_index"             : receivedInput['transaction_index'],
    "from_address"                  : receivedInput['from_address'],
    "to_address"                    : receivedInput['to_address'],
    "value"                         : f' {shares_for_sale} For {asking_price} / {ratio}',
    "gas"                           : receivedInput['gas'],
    "gas_price"                     : receivedInput['gas_price'],
    "block_timestamp"               : timestamp(receivedInput['block_timestamp'])
    }

	return result

	#COMPLETED

#----------------------------------------------------------------------------------------------------

def masternodeCreate(receivedInput):

	tier = receivedInput["input"]
	tier = tier[73]
	DESCRIPTOR = f'Masternode Created Tier {tier}'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#------------------------------------------------------------------------------------------------------

def masternodeTerminate(receivedInput):
	DESCRIPTOR = "MASTERNODE Terminated"


	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Terminated",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result



#------------------------------------------------------------------------------------------------------------

def masternodeSuspend(receivedInput):
	DESCRIPTOR = "MASTERNODE Suspended"


	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Suspended",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result



#------------------------------------------------------------------------------------------------------------
#DEX

def dexPlaceOrder(receivedInput):
	DESCRIPTOR = "Dex Order Placed"

	data = receivedInput["input"]
	answer = parse(data)
	orderNumber = str(answer[4])
	Wanting =  tokenType(dectohex(answer[0]))
	shares_wanted = int(answer[1])
	shares_wanted2 = str(Web3.fromWei(shares_wanted, 'Ether'))
	giveCoin = int(answer[3])
	giveCoin2 = str(Web3.fromWei(giveCoin, 'Ether'))
	Giving = tokenType(dectohex(answer[2]))
	
	

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
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	#"input"					: {"orderNumber": answer[4], "amountWanted": shares_wanted2, "wantCoin": Wanting,  "amountGiving": giveCoin2, "giveCoin": Giving }
	}

	

	return result


def dexOrderCancelled(receivedInput):

	DESCRIPTOR = "HaloDex Order Cancelled"

	value					= "Cancelled Order"
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#------------------------------------------------------------------------------------------------------------



def ethOffNetwork(receivedInput): #"0xb36c2acc": 	ethOffNetwork

	DESCRIPTOR = "H-ETH sent to ETH Chain"

	data = receivedInput["input"]
	answer = parse(data)


	value					= int(answer[1])
	value 					= value / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	description 			= "H-ETH sent to ETH Chain"
	eth 					= data[34:74]
	eth_address = 			"0x" + eth

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: eth_address,
	"value"					: value,
	"gas" 					: eth_address,
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description,
	"external"				: "https://etherscan.io/address/{}".format(eth_address)
							}

	
	return result


#------------------------------------------------------------------------------------------------------------


def ERCtoChain(receivedInput): 

	inputs = receivedInput['input']
	contract = receivedInput["to_address"]
	token = tokenType(contract)
	
	DESCRIPTOR = (f'{token} --> ETH Network')

	#DESCRIPTOR = "ERC20 to ETH Chain"

	data = receivedInput["input"]
	answer = parse(data)


	value					= int(answer[1])
	value 					= Web3.fromWei(value, 'ETHER')
	description 			= "H-ETH sent to ETH Chain"
	eth 					= data[34:74]

	eth_address = 			"0x" + eth

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: eth_address,
	"value"					: value,
	"gas" 					: eth_address,
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description,
	"external"				: "https://etherscan.io/address/{}".format(eth_address)
							}

	
	return result


#------------------------------------------------------------------------------------------------------------
#ETH

def ethTransferWallettoDex1(receivedInput): #"0x095ea7b3"
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	realvalue = int(contract[1])
	token = tokenType(receivedInput["to_address"])
	DESCRIPTOR = f'{token} --> HaloDex SC'
	
	value					= Web3.fromWei(realvalue, 'Ether')
	description = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	if token == "FCT" :
            balance = value * 10000000000
            value = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description	
	}

	return result
#------------------------------------------------------------------------------------------

def ethTransferWallettoDex2(receivedInput):

	inputs = receivedInput['input']
	contract = parse(inputs)
	token2 = dectohex(contract[0])
	token = tokenType(token2)
	
	DESCRIPTOR = (f'{token} Deposit --> HaloDex')
	realvalue = int(contract[1])
	value					= Web3.fromWei(realvalue, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	if token == "FCT" :
            balance = value * 10000000000
            value = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
            

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#---------------------------------------------------------------------------------------------

def hethToEth(receivedInput): #0x9e281a98
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	token2 = dectohex(contract[0])
	token = tokenType(token2)
	DESCRIPTOR = (f' {token} Withdrawl From HaloDex')
	
	realvalue = int(contract[1])
	value					= Web3.fromWei(realvalue, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#------------------------------------------------------------------------------------------------	
def dexPlaceOrder1(receivedInput): #"0x0b927666": 	dexPlaceOrder,
	DESCRIPTOR = "Dex Order Placed "

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	value					= "Order Placed"

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result





def dexFilledOrder(receivedInput): #"0x31663639": 	dexFilledOrder,
	DESCRIPTOR = "Dex Order Filled "

	inputs = parse(receivedInput["input"])
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	value					= "Order Filled"
	giveCoin = tokenType(dectohex(inputs[1]))
	values = int(inputs[11])
	weis	= dectohex(inputs[5])
	giveValue = Web3.fromWei(values, 'ETHER')
	receivedCoin = tokenType(dectohex(inputs[3]))
	value2 = int(inputs[4])
	receivedValue = Web3.fromWei(value2 , 'ETHER')
	tradePartner = dectohex(inputs[7])
	price = giveValue/receivedValue

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
	#"input"					: f' {giveValue} {giveCoin} For {receivedValue} {receivedCoin} Buyer/Seller = {tradePartner} Price = {price}',
							}

	
	return result


#GAMES

def gamesDeposit(receivedInput):
	
	DESCRIPTOR = "Block And Chain Deposit"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}
							

	
	return result


def WrappedTokenTransfer(receivedInput):
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	toAddress = dectohex(contract[0])
	token = tokenType(receivedInput["to_address"])
	 

	DESCRIPTOR = (f' {token} Transfer Between Halo Wallets')
	amount = int(contract[1])
	value					= Web3.fromWei(amount, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: toAddress,
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result



def boughtMarketplace(receivedInput):
	
	DESCRIPTOR = "Marketplace MN Purchase"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result


def serviceFee(receivedInput):
	

	fee = parse(receivedInput["input"])
	fee = int(fee[3])
	value = "Fee"
	DESCRIPTOR = "SF"
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result


def bcwithdrawl(receivedInput):

	bandc = parse(receivedInput["input"])
	to_address = dectohex(bandc[3])
	value = int(bandc[2])
	DESCRIPTOR = "Block And Chain Withdraw" 

	value					= Web3.fromWei(value, 'Ether')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['to_address'],
	"to_address"			: to_address,
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result




def nodeActivate(receivedInput):
	
	DESCRIPTOR = "Node Activated"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Activated",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

def contractDeployment(receivedInput):
	
	DESCRIPTOR = "Contract Deployed"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Deploment",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result




Inputs	= {
	
	"0x": 			interHalo, #Done
	"0x0029185b": 	noInfo,	
	"0x00e77545": 	bcwithdrawl,	
	"0x0309bebc": 	noInfo,	
	"0x03e985d9": 	noInfo,	
	"0x04e27777": 	noInfo,	
	"0x06862706": 	noInfo,	
	"0x095ea7b3": 	ethTransferWallettoDex1,
	"0x338b5dea":   ethTransferWallettoDex2,
	"0x0b927666": 	dexPlaceOrder,
	"0x0c8e8326":	noInfo,
	"0x0c8e8326": 	ERCtoChain,
	"0x13a30791": 	noInfo,
	"0x19f7ae27": 	noInfo,
	#"0x2a95599f": 	MarketplaceCancelOrder,
	"0x2e1a7d4d": 	haloFromDexToWallet,
	"0x31663639": 	dexFilledOrder,
	"0x44811585": 	serviceFee,
	"0x4b67e07f": 	noInfo,
	"0x4d4ea199": 	noInfo,
	"0x4e656f5f": 	noInfo,
	"0x5848e444": 	noInfo,
	"0x5bd05f7f": 	noInfo,
	"0x60606040": 	contractDeployment,
	"0x61443a5f": 	noInfo,
	"0x65863672": 	noInfo,
	"0x68627069": 	noInfo,
	"0x6d69fcaf": 	noInfo,
	"0x6f0ef949": 	noInfo,
	"0x726c4d6f": 	CommitToSharedContract,
	"0x749726fe": 	noInfo,
	"0x76319190": 	noInfo,
	"0x763819ea": 	masternodeCreate,
	"0x792fa508": 	masternodeSuspend,
	"0x7c325d0e": 	masternodeTerminate,
	"0x7f746573": 	noInfo,
	"0x8255069d": 	dexOrderCancelled,
	"0x9407ea98": 	noInfo,
	"0x976640e2": 	noInfo,
	"0x98ca05eb": 	ERCDeposit,
	"0x99404220": 	noInfo,
	"0x9e281a98": 	hethToEth,
	"0x9f8a89ba": 	nodeActivate,
	"0xa9059cbb": 	WrappedTokenTransfer,
	"0xb214faa5": 	gamesDeposit,
	"0xb36c2acc": 	ethOffNetwork,
	"0xb5ec9999": 	noInfo,
	"0xc885bc58": 	masternodePayout,
	"0xc94ee098": 	noInfo,
	"0xcbb0f029": 	boughtMarketplace,
	"0xceeb7066": 	noInfo,
	"0xd0e30db0": 	HaloWalletToDex,
	"0xd4444da6": 	masternodeSell,
	"0xdf6c39fb": 	payout,
	"0xea115fdb": 	DepositEth,
	"0xf612f5ce": 	noInfo,
	"0xff3252a1": 	noInfo,
	"0x68627069":   systemPing,
	"0xd28c25d4":	SmartContract,
	"0x60806040": 	ContractDeploy,
	"0x42966c68" : Burn


}
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ETHER _ 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#MMMMMMMMMMMMMMMMm/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMh/-.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMy:/-..yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMs///:---sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMNs///+:::::oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMmooo+++/::///oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMhyMMMMM/ NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN--+MMMM
#MMMMMMd++ooo+o+/////+omMMMMMMMMMMMMMMMMMMMMMMMMMMM:"MMMMM/ NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""MMMM
#MMMMMh//+oosoo++++++++omMMMMMMMMMMMMMs+++++++sNMM+. +omMM/ Nho///+sMMMNs+++++++sNMMMNs+++MMMMMMMMMMM""MMMM
#MMMMs://+oossso+oooooooodMMMMMMMMMMMo sNNNNNs oMMm-'mmNMM/ :smNNNs sMMo sNNNNNs oMMMo sNNMMMMMMMMMMM""MMMM
#MMMo-://+oossssoooossssssdMMMMMMMMMMo dMMMMMm +MMM:'MMMMM/ NMMMMMd oMM+ dMMMMMm +MMM+ mMMMMMMMMMMMMM''MMMM
#MMMMNhs++oossysssssssydmMMMMMMMMMMMMo +ooooo+ +MMM:'MMMMM/ NMMMMMd oMM+ +ooooo+ +MMM+ mMMMMh:::+MMMM""MMMM
#MMMNmmMMNdyssyyssyhmNMNmmNMMMMMMMMMMo ydddddddmMMM:'MMMMM/ NMMMMMd oMM+ ydddddddmMMM+ mMMMMMMMMMMMMM""MMMM
#MMMMMdhhdmMMNmdmNMMNdhhdMMMMMMMMMMMMo dMMMMMNshMMM:'MMMMM/ NMMMMMd oMM+ dMMMMMNshMMM+ mMMMMMMMMMMMMM""MMMM
#MMMMMMdyyyoshmMmdhyyyymMMMMMMMMMMMMMy /hhhhh+ sMMM/ ohdMM/ NMMMMMd oMMs /hhhhh/ sMMy: sdMMMMMMMMMMMs""sMMM
#MMMMMMMmsoo+++NsssssyNMMMMMMMMMMMMMMMdyyyyyyydMMMMMdyyhMMdhMMMMMMNhmMMMdyyyyyyydMMMhhhhmMMMMMMMMMMMhhhhMMM
#MMMMMMMMNs+///N++++yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMy/::N///hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMd:-N-/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMN/m+NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

import codecs
def EthoFuse(receivedInput):
	
	DESCRIPTOR = "Etho-Fuse Game"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result	



def blockMined(receivedInput):
	
	
	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	web3 		= 	one_connect_geth()
	db 			= 	"ether1-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol 		= 	mydb["temp"]
	myCol2 		= 	mydb["block_rewards"]
	bn 			= 	receivedInput['number']

	reward = "Unknown Not DB"
	try:
		for x in myCol2.find({"block_number": bn}):
			reward = " {} ETHO".format(x["reward"][:5])
	except:
		reward = "Unknown"

	DESCRIPTOR = "New Block Mined"
	try:
		extra_data			= receivedInput['extra_data'][2:]
		value 					= codecs.decode(extra_data, "hex").decode('utf-8')

		#value 					= receivedInput['value'] / 1000000000000000000
		#value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	except:
		value = "Miner Unknown"

		#description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_number"			: receivedInput['number'],
	"from_address"			: receivedInput['miner'],
	"value"					: value,
	"reward" 				: reward,
	"block_timestamp"		: onetimestamp(receivedInput['timestamp']),
	"description"			: "BlockMined",
	"difficulty"			: receivedInput['difficulty'] / 1000000000

	}

	
	return result	


def onenoInfo(receivedInput):

	DESCRIPTOR = "PLEASE REPORT BLOCK NUMBER AND A BREIF SUMMARY OF WHAT YOU THINK THIS IS"
	description = f'Unknown At the Current Time'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
#------------------------------------------------------------------------------------------------------------



def Masternode(receivedInput):

	DESCRIPTOR = "Masternode Related. No Further Details"
	description = f'Unknown At the Current Time'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
OneInputs	= {
	'blockmined':   blockMined,
	'0xa6f2ae3a':	onenoInfo,
	'0x2f54bf6e':	onenoInfo,
	'0x43214675':	onenoInfo,
	'0x1986a58c':	onenoInfo,
	'0xc4d66de8':	onenoInfo,
	'0xb61d27f6':	onenoInfo,
	'0x60806040':	onenoInfo,
	'0xa1adbb25':	onenoInfo,
	'0x2e1a7d4d':	onenoInfo,
	'0x3ccfd60b':	onenoInfo,
	'0x793cd71e':	onenoInfo,
	'0xcb1fa1d8':	onenoInfo,
	'0xcc9ab267':	onenoInfo,
	'0xb18759de':	onenoInfo,
	'0x486579'	:	onenoInfo,
	'0xb75c7dc6':	onenoInfo,
	'0x06ab5923':	onenoInfo,
	'0xf05834d6':	onenoInfo,
	'0xa9059cbb':	onenoInfo, #-TokenTransfer,
	'0x6dd5e67c':	onenoInfo,
	'0x746970' 	:	bot_tip,
	'0xccb726b1':	onenoInfo,
	'0x57618e1d':	onenoInfo,
	'0xf2fde38b':	onenoInfo,
	'0xfdb5a03e':	EthoFuse,
	'0x19b667da':	onenoInfo,		
	'0x60606040':	onenoInfo,
	'0x797af627':	onenoInfo,
	'0x467fba0f':	onenoInfo,
	'0x424c4f43':	onenoInfo,
	'0x6703777d':	onenoInfo,
	'0x604c602c':	onenoInfo,
	'0x48657920':	onenoInfo,
	'0x507ffba5':	onenoInfo,
	'0x29ff4f53':	onenoInfo,
	'0x8d036731':	onenoInfo,
	'0x49ade46d':	onenoInfo,
	'0x60748060':	onenoInfo,
	'0xfdacd576':	onenoInfo,
	'0x0a9ef927':	onenoInfo,
	'0x4e71d92d':	EthoFuse,
	'0x'		:	etherOneTx,
	'0x04fc7c6d':	onenoInfo,
	'0x230d6ed8':	onenoInfo,
	'0xd65ab5f2':	onenoInfo,
	'0xd420a7e6':	onenoInfo,
	'0xc375c2ef':	Masternode,
	'0xd0e30db0':	onenoInfo,
	'0x55c081d4':	onenoInfo,
	'0x6102cb61':	onenoInfo,
	'0x940c70f3':	onenoInfo
}
