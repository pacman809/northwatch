#!/usr/bin/python3.6


from web3 import Web3

#UNHASH URL OR CREATE YOUR OWN
#------------------------------------------------

#geth_url = "http://mainnet.haloplatform.tech"		#HaloPlatform's shitty node. Only good for Block number
geth_url = "http://192.168.0.58:8545"				#Full Blown Node good for everything
#geth_url = ""
#geth_url = ""
#geth_url = ""
#geth_url = ""


#------------------------------------------------


try:
	web3 = Web3(Web3.HTTPProvider(geth_url))
	print(web3.eth.blockNumber)
except:
	print("WEB3 CONNECTION ERROR")




