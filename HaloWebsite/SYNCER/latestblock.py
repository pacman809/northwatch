#!/usr/bin/python3.6


from web3 import Web3


#geth_url = "http://mainnet.haloplatform.tech"
#geth_url = "http://206.45.86.254:80"
geth_url = "http://192.168.1.103:8545"
web3 = Web3(Web3.HTTPProvider(geth_url))

print(web3.eth.blockNumber)


