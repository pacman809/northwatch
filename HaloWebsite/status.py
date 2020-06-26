from web3 import Web3

#RPC NODE URL
GethUrl 	= "http://192.168.0.58:8545" #Halo
OneGethUrl 	= "http://192.168.0.58:8585" #ETHER1
TwoGethUrl  = "http://192.168.0.58:8645" #EGEM


def NodeStatus():

	try:
		web3 = Web3(Web3.HTTPProvider(GethUrl))
		Halo = web3.eth.blockNumber
	except:
		Halo = "OFFLINE"

	try:
		web4 = Web3(Web3.HTTPProvider(OneGethUrl))
		Ether1 = web4.eth.blockNumber
	except:
		Ether1 = "OFFLINE"

	try:	
		web5 = Web3(Web3.HTTPProvider(TwoGethUrl))
		Egem = web5.eth.blockNumber
	except:
		Egem = "OFFLINE"
			
	status = {

	"Halo": 	Halo ,
	"Ether1":	Ether1 ,
	"Egem":		Egem

	}

	return status
