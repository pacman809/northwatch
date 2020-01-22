#!/usr/bin/env python3

#CONFIG HERE FOR WEB RPC CONNECTION



from web3 import Web3

def connect_geth():
	#geth_url = "http://206.45.86.254:80"
	#geth_url = "http://mainnet.haloplatform.tech" #Halo RPC
	geth_url = "http://192.168.1.103:8545"
	#geth_url = "http://localhost:8545"
	#geth_url = "http://192.168.1.139:8545"
	web3 = Web3(Web3.HTTPProvider(geth_url))
	return web3
	


