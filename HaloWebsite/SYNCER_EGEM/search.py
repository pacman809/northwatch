#!/usr/bin/env python3

from web3 import Web3

def connect_geth():
	#geth_url = "http://206.45.86.254:80"
	#geth_url = "mainnet.haloplatform.tech"
	#geth_url = "http://192.168.1.231:8545"
	#garth@192.168.1.231
	geth_url = "http://192.168.0.58:8645"
	#geth_url = "http://192.168.1.103:8545"
	web3 = Web3(Web3.HTTPProvider(geth_url))
	return web3
	


