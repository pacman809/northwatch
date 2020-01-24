#!/usr/bin/python3.6


from web3 import Web3

#UNHASH URL OR CREATE YOUR OWN
#------------------------------------------------

#geth_url = "http://mainnet.haloplatform.tech"		#HaloPlatform's shitty node. Only good for Block number
#geth_url = "http://192.168.1.139:8545"				#Full Blown Node good for everything
geth_url = "http://192.168.1.103:8545"
#geth_url = ""
#geth_url = ""
#geth_url = ""


#------------------------------------------------



web3 = Web3(Web3.HTTPProvider(geth_url))#print(f'Block Number		={web3.eth.blockNumber}')

print(web3.isConnected())




